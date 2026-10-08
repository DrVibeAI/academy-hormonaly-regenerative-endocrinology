# Account navigation — 7 October 2026

Omar requested the same name-menu behavior as BioLongeva. The local Hormonaly runtime now reuses BioLongeva's deployed account components with Arabic labels and Hormonaly colors. The four learning destinations are Today, Course, Library and Guide. The name opens Profile, Certificate, Settings and Help; authorized account actions remain available.

Arabic desktop popover and mobile bottom sheet verified, including certificate/settings jumps, keyboard focus containment and Escape closure. No horizontal overflow. Type, isolation, locale and build checks pass. This is a deliberate UI change on top of the verified Hormonaly baseline, not a claim that production already has it. Production remains unchanged.

Follow-up: fixed the local-mode badge overlapping the mobile menu. The modal now renders above fixed status banners; opaque surface and viewport bounds verified in the browser. See account-menu-overlap-fixed.jpg.

Rechecked during the QA repair pass: current evidence is in fixes-20261007/account-menu-mobile.png and fixes-20261007/account-menu-desktop.png. Both menu surfaces cover the local-mode banner. The current review archive includes these and account-menu-overlap-fixed.jpg.
