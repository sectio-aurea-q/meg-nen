# S070 (Gelb et al. 1982): page 375 and the correction notice — 18 November 2026

Follows `curation/2026-11-16_fernleihe_S003-S005_S066-S070/`. That record left S070 without rows: Table I
prints no temperature, Table II holds label ratios, and page 375 was missing from the paper copy. The page and
the correction notice have now been read. Nothing is entered; the reasons are below.

## What was read

- Page 375 of S070 (Biochemistry 1982, 21, 370–377, doi 10.1021/bi00531a026), re-ordered through interlibrary
  loan and photographed by the author on 18 November 2026.
- The entry for S070 on a "Corrections" page of Biochemistry, volume 21 (1982), photographed the same day. The
  same page corrects papers up to volume 21, number 3 (2 February 1982). The page number is not on the photo;
  Crossref lists the notice as volume 21, number 12 (8 June 1982), page 3036, doi 10.1021/bi00541a607.
- Pages 372, 373 and 374 once more, from the photos of 15 November 2026, only for the drawings and the
  definitions.

Both new pages were read by the curator (rule 3), each twice from the photo; the second look knew the first.
This is not a blind second reading under rule 2. None was needed, because no value is entered.

## Page 375

Discussion and equations. The page has no table, states no temperature and prints no isotope effect measured in
S070.

- It discusses why the intermolecular effect is small (suppression in the steady state). It says that the
  effect is no different in single-turnover experiments that start from the oxygenated ferrous enzyme, and
  that none is found with the other oxidants by a competitive method. No number is given for this on the page.
- It cites one range from other work: an intramolecular effect of 1.6–2.0 for N-demethylation by liver
  cytochrome P450 (Miwa et al. 1980). Not entered (rule 1).
- It defines four net rate constants for a reversible hydrogen abstraction and writes A and B with them,
  together with the two limits (reverse step much slower, or much faster, than the steps that follow).
  Equations only.

## The correction notice

The notice refers to page 374. For the case without an intermolecular isotope effect, the equations for the
correction of incomplete labelling of the substrate are to read

    A = (aK + cL) / (a(1 − K) + c(1 − L) + b)
    B = (dK + fL) / (d(1 − K) + f(1 − L) + e)

    K = kH,endo / (kH,endo + kD,exo)        L = kH,exo / (kH,exo + kD,endo)

    I_exo = [K / (1 − K)] · G               I_endo = [L / (1 − L)] · (1/G)

It ends: "None of the conclusions in the paper are affected."

The symbols are those of page 374. A and B are the measured ratios of alcohol-d1 to alcohol-d0 in the product
from the mainly exo-labelled and the mainly endo-labelled substrate (Table II). a, b and c are the fractions of
5-exo-d1, d0 and 5-endo-d1 in the first substrate, d, e and f the same fractions in the second (printed:
a = 0.84, b = 0.04, c = 0.10, d = 0.05, e = 0.02, f = 0.93). G = kH,exo/kH,endo, I_exo = kH,exo/kD,exo and
I_endo = kH,endo/kD,endo. With pure labels A = kH,endo/kD,exo and B = kH,exo/kD,endo.

The equations the notice replaces, as printed on page 374:

    A = (a·kH,endo + c·kH,exo) / (a·kD,exo + b·(kH,exo + kH,endo) + c·kD,endo)
    B = (d·kH,endo + f·kH,exo) / (d·kD,exo + e·(kH,exo + kH,endo) + f·kD,endo)

    I_exo  = A·B·G·(af − dc) / (p·f·B − c·q·A)
    I_endo = A·B·(cd − fa) / (p·d·B − a·q·A)
    p = a + cG − A·b·(1 + G)                q = d + fG − B·e·(1 + G)

Note by the curator. The equations of page 374 are consistent among themselves: its I_exo and I_endo follow
from its A and B by algebra (checked symbolically). The notice is therefore not the repair of a misprint. It
changes how the label fractions enter: page 374 weights each labelled species with its rate constants, the
notice with its fraction alone. This is the curator's reading of the two sets of equations, not a statement of
the source.

## Which substrate is which

The tables show the substrates as drawings only. The paper's own drawings settle the assignment: the exo
substituent at C-5 is drawn to the side and the endo substituent downwards. Scheme II (page 374) shows it: the
substrate that reacts with kD,exo has D at the side, the one that reacts with kD,endo has D below. So does the
fourth substrate of Table I, 5-exo-bromocamphor-5-endo-d1, with Br at the side and D below.

- Table I (page 372), Vmax(H)/Vmax(D): camphor-5-exo-d1 1.23 ± 0.05; camphor-5-endo-d1 1.16 ± 0.05;
  camphor-5,6-endo-d2 1.13 ± 0.05; 5-exo-bromocamphor-5-endo-d1 1.15 ± 0.05.
- Table II (page 373): the first substrate is camphor-5-exo-d1 (ratio A), the third is camphor-5-endo-d1
  (ratio B).

Reading 2B of 16 November gave the same assignment and called one identification in Table I uncertain; with
the drawings compared it is no longer open.

## Decision

No row for S070.

- Table I holds isotope effects on Vmax from the NADH-driven turnover. No page of the paper states the
  temperature of these turnovers or of the reactions with the other oxidants (rule 11). The only temperature
  stated for a kinetic experiment, 10 °C, belongs to the single-turnover experiments; for these the paper
  prints two rates and no isotope effect.
- Table II holds the label ratios A and B. They combine two positions and are not isotope effects of one step.
  I_exo and I_endo appear only as curves against G in Figure 2 (rule 4), and they depend on G, which the paper
  does not determine.
- Page 375 and the correction notice add equations and no measured value.

S070 stays in `sources/first_sources.csv` as a source that was read and holds no row.

## Open

- The page number of the correction notice (3036) and its DOI come from Crossref, looked up on 18 November
  2026. Neither is on the photo. The page number is still to be compared with the paper copy.
