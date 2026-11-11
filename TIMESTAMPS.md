# Timestamps

Each working archive of this database written on or after 9 November 2026 is timestamped with [OpenTimestamps](https://opentimestamps.org),
which anchors the archive's SHA-256 digest in the Bitcoin blockchain. A confirmed timestamp shows that the
digest existed no later than the named block. It shows nothing about when the work began, and it says
nothing about whether the contents are correct.

## How to check one

    shasum -a 256 MEG-NEN_<date>_<time>.zip     # must match the digest below
    ots info MEG-NEN_<date>_<time>.zip.ots      # shows the Bitcoin block(s)
    ots verify MEG-NEN_<date>_<time>.zip.ots    # needs a local Bitcoin node

Four independent calendars are used, so a proof usually names several blocks; the earliest is the binding
one. `ots verify` needs a full Bitcoin node and is therefore not run here; `ots info` reporting a
`BitcoinBlockHeaderAttestation` is the proof itself and can be checked by anyone against a block explorer.

## Archives

Stamping began on 9 November 2026. The eleven archives of 6 to 8 November 2026 were written before that and
carry no proof; they are working backups, not evidence.

| archive | SHA-256 | earliest Bitcoin block |
|---|---|---|
| `MEG-NEN_2026-11-09_06-28.zip` | `080943b2a724dccc2f51150d1354a5672427877ccca72b5e602cc0da2c9084f0` | 975142 |
| `MEG-NEN_2026-11-09_07-10.zip` | `eaecc383390c43faad05701f2b771b71dff4ee63290d87cd97e864df5ce093ec` | 975142 |
| `MEG-NEN_2026-11-09_08-03.zip` | `f1b7f4490de0307fb79255880a4c655284514a93596f3535c44b313ebd088644` | 975147 |
| `MEG-NEN_2026-11-09_12-26.zip` | `fce0259761fe1cebdcbf1de1fb5f12e5b3ac06216b9092f42a2e63f305e8433a` | 975172 |
| `MEG-NEN_2026-11-09_13-06.zip` | `34725ef86dfcb8717a4650f57fe68df4a459c21699e02011c4063704f24a245c` | 975173 |
| `MEG-NEN_2026-11-09_13-30.zip` | `5f827f1ee4090f07254ef70e6fa8fe26ac475759f0a69fc3fe3aca77f8e9895a` | 975184 |
| `MEG-NEN_2026-11-09_14-06.zip` | `56626d8ad2d7f0cffa775c8dcc8be67e7ea045e0ec2dec6e3951c8238d5a491a` | 975184 |
| `MEG-NEN_2026-11-09_17-36.zip` | `ed9bdf4a59d28762c06198e336086ff2e7cb97b16b5563758f54b23f3bad68c0` | 975200 |
| `MEG-NEN_2026-11-09_17-38.zip` | `6e00a48eaacebe0d46d1b54e36047cacf9a7037dd66f3a6489888c7047d7eb75` | 975200 |
| `MEG-NEN_2026-11-09_21-27.zip` | `50ac82fae8bcd4cdab49fde7dc56a4d2959ee4e38b1c8ab6c924ecca453fffe7` | 975221 |
| `MEG-NEN_2026-11-10_10-44.zip` | `084922069fe504e66e17b42ef103f82e4595939ad9450b27c5ae925dab426c60` | 975284 |
| `MEG-NEN_2026-11-10_10-59.zip` | `11c5cf10539faa5373a0150babe2ff4fe02c1f5afa68866ea173952e431b1124` | 975284 |
| `MEG-NEN_2026-11-10_18-08.zip` | `c0d84be55f002b63a79ef0453f2bae2ba40ae3557ad8fd3f65f48446c82c5b5e` | 975328 |

A proof shown as pending carried the calendars' signatures but not yet a block when this file was
written; `ots upgrade` fetches the block once one has confirmed it, which normally takes a few hours. The
proof of the archive that contains this file is pending when the archive is cut, for that reason.

The archive that contains this file cannot carry its own digest here. Its digest is recorded outside the
archive, in the data note that cites it, and is added to the table above when the next archive is written.

The `.ots` proof files are kept beside the archives and are released with the database. The separate
`MEG-NEN_Quellen_*` archives hold the source papers; under rule 8 of `CURATION.md` those are never
published, and their digests are not listed here.
