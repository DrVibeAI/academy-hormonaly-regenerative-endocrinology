#!/usr/bin/env python3
"""Offline mutation tests. agent pre-review — no gate opened.

Only three bound source files are copied to temporary directories. The temporary
.git pointer reads existing local objects; no refs, index or real source is written.
"""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PACKAGE = 'packages/hormones-peptides-skin.json'
LOCK = 'course-production/hormones-peptides-skin/source-lock.md'


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='hormonaly-refresh-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'academy'
        for rel in (PACKAGE, LOCK, 'foundry.lock'):
            dest = self.repo / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((REPO / rel).read_bytes())
        git_dir = subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', '--absolute-git-dir'], text=True).strip()
        (self.repo / '.git').write_text('gitdir: ' + git_dir + '\n')
        self.proposal = json.loads((HERE / 'audio-beats-proposal.json').read_bytes())
        self.path = self.root / 'proposal.json'

    def run_validator(self, *args):
        self.path.write_text(json.dumps(self.proposal, ensure_ascii=False))
        return subprocess.run([sys.executable, str(HERE / 'validate_proposal.py'),
                               '--repo', str(self.repo), '--proposal', str(self.path), *map(str, args)],
                              capture_output=True, text=True)

    def rejects(self, expected, *args):
        result = self.run_validator(*args)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('FAIL ' + expected, result.stdout)
        self.assertNotIn('WROTE', result.stdout)

    def test_current_package_passes(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('OK: 0 failure(s)', result.stdout)

    def test_changed_beat_text_fails(self):
        self.proposal['blocks']['m4-p06']['proposedAudioBeats'][0]['body']['en'] += ' Changed.'
        self.rejects('all seven beats')

    def test_changed_title_fails(self):
        self.proposal['blocks']['m4-p06']['proposedAudioBeats'][0]['title']['en'] = 'Changed'
        self.rejects('all seven beats')

    def test_reordered_whole_source_beats_fail(self):
        # Still verbatim, valid qualifiers and valid source maps: exact reuse must fail.
        entry = self.proposal['blocks']['m4-p06']
        entry['proposedAudioBeats'].reverse()
        entry['beatSources'].reverse()
        self.rejects('all seven beats')

    def test_changed_citation_fails(self):
        refs = self.proposal['blocks']['m4-p06']['citationRefs']
        refs[0] = 'bjerke-2026-cosmetic-peptide-safety-framework'  # exists, but belongs to the other block
        self.rejects('m4-p06: citationRefs identical')

    def test_stale_block_bindings_fail(self):
        for field in ('sourceFingerprint', 'bodySha256', 'audioScriptSha256'):
            with self.subTest(field=field):
                original = self.proposal['blocks']['m4-p06'][field]
                self.proposal['blocks']['m4-p06'][field] = '0' * 64
                self.rejects({'sourceFingerprint': 'm4-p06: block fingerprint',
                              'bodySha256': 'm4-p06: body.en sha256',
                              'audioScriptSha256': 'm4-p06: audioScript.en sha256'}[field])
                self.proposal['blocks']['m4-p06'][field] = original

    def test_stale_source_bindings_fail(self):
        original = copy.deepcopy(self.proposal['source'])
        for field in ('sha256', 'bytes', 'gitBlob', 'baseCommit', 'sourceLock', 'foundryRef'):
            with self.subTest(field=field):
                self.proposal['source'] = copy.deepcopy(original)
                if field in self.proposal['refresh']['originalSource'] and field in ('sha256', 'bytes', 'gitBlob', 'baseCommit'):
                    self.proposal['source'][field] = self.proposal['refresh']['originalSource'][field]
                elif field == 'sourceLock':
                    self.proposal['source'][field]['sha256'] = '0' * 64
                else:
                    self.proposal['source'][field] = '0' * 40
                self.rejects('proposal is exact original plus four source bindings')

    def test_approval_fields_fail(self):
        for field in ('approvals', 'approvalStatus', 'approval_status', 'approvedBy', 'approvedOn'):
            with self.subTest(field=field):
                self.proposal['blocks']['m4-p06'][field] = [] if field == 'approvals' else 'test-only'
                self.rejects('no approval fields')
                del self.proposal['blocks']['m4-p06'][field]

    def test_status_and_governance_additions_fail(self):
        self.proposal['status'] = 'test-only'
        self.proposal['governance'] = {'approvals': []}
        self.rejects('proposal is exact original plus four source bindings')

    def test_changed_original_provenance_fails(self):
        self.proposal['refresh']['originalSource']['sha256'] = '0' * 64
        self.rejects('proposal is exact original plus four source bindings')

    def test_package_teaching_drift_fails(self):
        path = self.repo / PACKAGE
        raw = path.read_bytes()
        path.write_bytes(raw.replace(b'Serum yes, syringe no.', b'Serum yes, syringe XX.', 1))
        self.rejects('watch-only drift')

    def test_watch_metadata_drift_fails(self):
        path = self.repo / PACKAGE
        path.write_bytes(path.read_bytes().replace(b'"weekly"', b'"yearly"', 1))
        self.rejects('current package bytes equal pinned base')

    def test_changed_lock_bytes_fail(self):
        path = self.repo / LOCK
        path.write_bytes(path.read_bytes() + b'\n')
        self.rejects('source lock bytes equal original')

    def test_missing_offline_history_fails(self):
        (self.repo / '.git').unlink()
        self.rejects('invalid input or unavailable offline Git history')

    def test_emit_inside_repo_fails(self):
        self.rejects('--emit-applied target', '--emit-applied', self.repo / 'preview.json')
        self.assertFalse((self.repo / 'preview.json').exists())

    def test_failed_validation_never_emits(self):
        self.proposal['blocks']['m4-p06']['sourceFingerprint'] = '0' * 64
        target = self.root / 'preview.json'
        self.rejects('m4-p06: block fingerprint', '--emit-applied', target)
        self.assertFalse(target.exists())

    def test_emit_copy_only(self):
        target = self.root / 'preview.json'
        before = (self.repo / PACKAGE).read_bytes()
        result = self.run_validator('--emit-applied', target)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        current, patched = json.loads(before), json.loads(target.read_bytes())
        def apply(node):
            if isinstance(node, dict):
                if node.get('type') == 'audio' and node.get('id') in self.proposal['blocks']:
                    node['audioBeats'] = self.proposal['blocks'][node['id']]['proposedAudioBeats']
                for value in node.values():
                    apply(value)
            elif isinstance(node, list):
                for value in node:
                    apply(value)
        apply(current)
        self.assertEqual(patched, current)
        self.assertEqual((self.repo / PACKAGE).read_bytes(), before)
        self.rejects('--emit-applied target already exists', '--emit-applied', target)


if __name__ == '__main__':
    unittest.main(verbosity=2)
