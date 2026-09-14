# Math Exam Coverage Tracker

Tracks which sub-topics have been tested in which exam, per [[exam-coverage-discipline]]. Built retroactively on 2026-07-17 while creating exam-13, by reading the full text of exam-01 through exam-04 and exam-10 through exam-12 (via `pdftotext -layout`) and cross-checking every new exam-13 question against that history. Updated 2026-07-28 for exam-14 (cross-checked against the full text of exam-01 through exam-13, all 13 prior papers, via `pdftotext -layout`). Update this file whenever a new math exam is built.

Exam key: 01=Ch1-2 (Real Numbers, Logarithms) | 02=Ch3-5 (Sets & Relations, Factorization, Linear Equations & Inequalities &mdash; Unit 3 Sets is no longer in the confirmed syllabus) | 03=Ch4-5-7 (Factorization, Linear Equations, Coordinate Geometry) | 04=Ch4 (Factorization only) | 10=Ch1-2-4-5-7-10 (comprehensive, includes Practical Geometry which is now excluded) | 11=Ch1-2-4-5-7 | 12=Ch1-2-4-5-7 | 13=Ch1-2-4-5-7 | 14=Ch1-2-4-5-7 (this build).

**Note:** Unit 3 (Sets & Relations), Unit 6 (Trigonometry), Unit 8 (Geometry of Straight Lines), Unit 9 (Geometry & Polygons), and Unit 11 (Basic Statistics) are outside Seemab's confirmed current syllabus and are not tracked here. **Unit 10 (Practical Geometry) is deliberately excluded from exam-13, exam-14 and all future exams** because Seemab has no geometry box &mdash; zero construction questions until Atif confirms otherwise.

## Unit 1 &mdash; Real Numbers

| Sub-topic | Tested in |
|---|---|
| Real numbers = union of rational & irrational | 01, 10, 11, 12 |
| Basic properties (closure, commutative, associative, identity, inverse) &mdash; identify/state | 01, 11, 12 |
| Distributive property a(b+c)=ab+ac | 01, 12 |
| Trichotomy property &mdash; verify with given values | 01, 13 (fresh: irrational values a=&minus;2&radic;3, b=&minus;5) |
| Properties of equality/inequality as a named "identify the property" short/MCQ question | 13 (transitive, multiplicative-of-inequality), **14 (fresh: symmetric property of equality as MCQ; cancellation w.r.t. multiplication of inequality as MCQ)** |
| Radicals: product/quotient rule, simplify, reduce index | 01, 11 |
| Laws of exponents (rational & negative exponents) | 01, 11, 12 |
| Scientific notation (MCQ identification & conversions) | 01, 11, **14 (fresh: 0.0000728 as MCQ)** |
| Number line representation of inequalities | 01 |
| Additive/multiplicative inverse concepts | 01, 12 |
| Multiplicative inverse of 0 (no inverse exists) | 13 |
| Radical &harr; exponential form: denominator of exponent = index of radical | 13 |
| TRUE/FALSE rational vs irrational statements with counterexample | 11, 12 |
| Application of real numbers in daily life (Exercise 1.3) | 13 (unit-rate word problem/Momina walk, ratio-sharing of a penalty, Fahrenheit/Kelvin temperature conversion), **14 (fresh, 6 more Exercise 1.3 items: bank-balance subtraction (Qasim), fabric cost-per-yard (Salma), balloon total cost, banner width & perimeter cost, hiking-club range reasonableness, Wajid&rsquo;s petrol-average reasonableness check)** |

**Unit 1 status:** Exercise 1.3 (Application of Real Numbers) is now essentially fully covered across exam-13 + exam-14 &mdash; 8 of its ~10 items have been used. Only the shoe-factory capital/debt item (source OCR garbled, fraction unclear) remains untested/unusable.

## Unit 2 &mdash; Logarithms

| Sub-topic | Tested in |
|---|---|
| Definition of logarithm, exponential &harr; logarithmic form | 01, 10 |
| Characteristic of a logarithm | 01, 10, 12 |
| log<sub>b</sub>1=0, log<sub>b</sub>b=1, base of natural log = e | 01 |
| Laws of logarithms (product, quotient, power) &mdash; expand/combine | 01, 10, 11, 12 |
| Evaluate using given log 2, log 3, log 5(, log 7) values | 01, 10, 11, 12, 13, **14 (fresh: log(63/20), log(84/25) &mdash; neither expression previously used)** |
| Digits in a<sup>n</sup> via logs | 01 (2<sup>20</sup>, 5<sup>37</sup>), 11 (3<sup>30</sup>), 13 (7<sup>40</sup>), **14 (fresh: 2<sup>60</sup> as MCQ, 6<sup>45</sup> in Section C)** |
| Richter-scale / earthquake-magnitude word problems | 01 (Pakistan 2005 vs China 1978; Kansu vs Tokyo) &mdash; **heavily recycled, deliberately avoided again in exam-13 and exam-14** |
| Evaluate complex log-table expressions (nth-root combinations) | 11, 12 |
| Scientific notation &harr; standard notation | 01, 10 |
| **Scientific-notation word application beyond Richter scale** (Exercise 2.1: recitation-count timing, Earth&ndash;Sun light-travel time) | **14 (first time &mdash; genuinely different real-world application from Richter scale, per the long-standing gap note; &lsquo;Kalma Pak&rsquo; recitation-count problem and light-travel-time problem, both from Exercise 2.1, had never been drawn from before)** |
| Antilogarithm (find antilog of a given value) | 13 (2.4324, 1.5890), **14 (fresh values: 3.5636, 2.9281)** |
| Domain / definedness of a log expression (log<sub>2</sub>(7&minus;x) for several x) | 13 |
| "Important results" identities (log<sub>c</sub>a &middot; log<sub>a</sub>b = log<sub>c</sub>b) | 13 |
| Find log of a given number via characteristic + mantissa (Exercise 2.3) | **14 (first time as its own question type: log 5313, log 1109)** |
| Antilog of a round/clean value tying back to a given log constant (log x = 2.4771 &rArr; x = 300, using log 3 = 0.4771) | **14 (first time &mdash; elegant use of the "given log values" set to backtrack an antilog)** |

## Unit 4 &mdash; Factorization & Algebraic Manipulation

| Sub-topic | Tested in |
|---|---|
| Type VI (a<sup>4</sup>+a<sup>2</sup>b<sup>2</sup>+b<sup>4</sup>, a<sup>4</sup>+4b<sup>4</sup>) | 03, 11 |
| Trinomial factorization x<sup>2</sup>+px+q, ax<sup>2</sup>+bx+c | 02, 03, 04, 10, 11, 12, 13 (x<sup>2</sup>&minus;11x+30), **14 (fresh: x<sup>2</sup>+2x&minus;15 MCQ, 2x<sup>2</sup>&minus;5x&minus;3, x<sup>2</sup>&minus;2x&minus;8, x<sup>2</sup>&minus;x&minus;12, 2x<sup>2</sup>+5x&minus;3, x<sup>2</sup>+2x&minus;3)** |
| Type IX (four-binomial products with substitution) | 02, 03, 04, 10, 11, 12 |
| Sum/difference of cubes | 02, 03, 04, 10, 11, 12, 13 (27+512x<sup>3</sup>, a<sup>6</sup>&minus;64), **14 (fresh: 8+y<sup>3</sup> MCQ)** |
| HCF by factorization | 02, 03, 04, 10, 11, 12, 13 (12x<sup>2</sup>+x&minus;1, 15x<sup>2</sup>+8x+1), **14 (fresh pairs: x<sup>2</sup>&minus;2x&minus;8 &amp; x<sup>2</sup>&minus;x&minus;12; 2x<sup>2</sup>+5x&minus;3 &amp; x<sup>2</sup>+2x&minus;3)** |
| HCF by division method | 04 |
| LCM by factorization | 02, 03, 04, 11 |
| Relation LCM&times;HCF = P&times;Q, find missing polynomial | 04, 10, 12, **14 (fresh, as a "given HCF & LCM, find the product P&times;Q" MCQ)** |
| Square root by factorization | 03, 04, 10, 11, 13 (25a<sup>4</sup>&minus;30a<sup>3</sup>+9a<sup>2</sup>), **14 (fresh: 16y<sup>2</sup>&minus;56y+49)** |
| Square root by division method | 03, 10 |
| Simplify algebraic fractions (&times;, &divide;, +, &minus;, DMAS) | 02, 04, 10, 12 |
| Application of factorization in daily life (Exercise 4.8) | 13 (cubical oil tank: volume &rarr; height &rarr; surface area &rarr; painting cost), **14 (first time for the other two Exercise 4.8 items &mdash; rectangular veranda area &rarr; dimensions &rarr; perimeter &rarr; fencing &amp; carpeting cost; square machine surface area &rarr; side &rarr; boundary &rarr; polishing &amp; edging cost)** |
| Conceptual property: HCF unchanged when polynomials are scaled by a constant | 13 |

**Unit 4 status:** all three Exercise 4.8 daily-life application items are now covered across exam-13 + exam-14. The wheel-radii and presser-dimension items (Q4, Q5) remain untested (source OCR was too garbled to safely reconstruct exact expressions) &mdash; candidates for a future paper once re-verified against a clean scan.

## Unit 5 &mdash; Linear Equations & Inequalities

| Sub-topic | Tested in |
|---|---|
| Linear equations with fractional coefficients | 02, 10, 11, 12 |
| Linear equations with decimal coefficients | 11, 12 |
| Radical equations &radic;(x+5)=4 style | 02, 11, **14 (fresh: 5&minus;&radic;(2x&minus;1)=0, Exercise 5.2 item, first genuinely new radical equation since exam-11; addresses the "radical equations under-tested vs absolute value" gap)** |
| Absolute value equations \|ax+b\|=c | 02, 03, 10, 11, 12, 13 (\|5x&minus;3\|=\|x+7\|, \|2y&minus;5\|=9), **14 (fresh: \|z+3\|&minus;3=5&minus;\|z+3\| [absolute value on both sides], 3\|z&minus;2\|&minus;4=&minus;2, \|5y\|=9, \|6&minus;3y\|=0 [MCQ, single-root case])** |
| Compound inequalities joined by "and"/"or" | 02, 03, 10, 11, 12, 13 (5x+10 &lt; &minus;35 or &gt; &minus;5), **14 (fresh: 3x+21&lt;1&minus;x or 3x+8&gt;3&minus;2x; 5&minus;3x&lt;11 or 2x+3&lt;&minus;9)** |
| **Double/combined compound inequality (already joined, e.g. 1 &le; 5&minus;3x &le; 22)** | **14 (first time &mdash; distinct from the "and"/"or" separate-clause style tested previously)** |
| Word problems (consecutive integers, bounded ranges) | 03, 12 |
| Word problem: "two times a number decreased by 5 &ge; number increased by 8" | 13 |
| Checking whether a given value satisfies an inequality (verify, don't solve) | 13 |
| **Set-builder notation for restricted domains (N, W, R)** | **14 (first time &mdash; Exercise 5.4 Q1(b): 2&le;x&lt;5 x&isin;N, x&le;4 x&isin;W, &minus;4&lt;x&le;3 x&isin;R)** |

## Unit 7 &mdash; Coordinate Geometry

| Sub-topic | Tested in |
|---|---|
| Distance formula | 03, 10, 11, 12, 13 (decimal-input midpoint pairing) |
| Midpoint formula | 03, 10, 11, 12, 13 (decimal coordinates (1.4,&minus;1.5) & (2.6,3.5)), **14 (fresh: A(3,4), C(x,y) with B(&minus;1,7) as midpoint, solve for C)** |
| Collinearity of three points | 03, 11, 12 |
| Prove vertices form a square / rectangle / parallelogram / rhombus | 03, 10, 11, 12, **14 (fresh rhombus: A(5,8), B(7,5), C(5,2), D(3,5), all sides &radic;13, plus diagonals AC=6, BD=4)** |
| Distance/midpoint of the hypotenuse of a right triangle | 12, **14 (fresh: X(7,4), Y(7,1), Z(&minus;3,1), hypotenuse XZ=&radic;109)** |
| Diameter/centre of a circle from its endpoints | 12 |
| Midsegment theorem (triangle midpoints, DE = &frac12;BC) | 12 |
| Quadrant identification from point signs | 13, **14 (fresh, Miscellaneous Ex.7 style: (&minus;4,&minus;(&minus;6)) MCQ; algebraic quadrant reasoning for (&minus;x,y) given x&lt;0,y&gt;0 MCQ)** |
| Segment-ratio reasoning at a midpoint (PR = PS &rArr; RS) | 13 |
| Missing 4th vertex of a rectangle found algebraically (not "prove all 4 given") | 13 |
| Midpoint quadrilateral / Varignon parallelogram | 13 (Exercise 7.2 Q2) |
| **"Label the missing coordinates" from a figure** (Exercise 7.2 Q7: Square OLMN, Rectangle ABCD) | **14 (first time &mdash; a previously-flagged gap; distinct from "solve algebraically for one unknown vertex" since here two full vertices must be read off the square/rectangle geometry)** |
| **Word problem: equidistant race-to-target-point** (Exercise 7.2 Q6, Hassan &amp; Ali) | **14 (first time &mdash; the other previously-flagged gap; starting points 6 units from origin on each axis, target = midpoint, verified via distance formula)** |

**Unit 7 status:** both previously-flagged gaps (square/rectangle missing-coordinate labelling, Hassan/Ali race problem) are now closed. Remaining fresh, unused Unit 7 material for a future paper: Miscellaneous Exercise 7 items on ordered-pair equality ((4,5)=((a+1)/2,b&minus;3)), abscissa-on-y-axis / d(A,C)&minus;d(B,C) collinear-point identities, minimum-distance-from-axis reasoning, kite-diagonal intersection point, and the trapezium/rhombus diagonal-bisection MCQs (Miscellaneous Ex.7 Q1(i)/(iii)/(iv)/(ix)/(x)/(xiii)/(xv)/(xvi)).

## Known remaining gaps (for future exams to prioritise)

- Unit 1: the shoe-factory capital/debt Exercise 1.3 item (source scan has a garbled fraction) &mdash; needs a clean re-scan before it can be used safely.
- Unit 2: the Richter-scale framing remains over-used from exam-01; the book only offers Richter-scale for a real-world log application, so exam-14 instead drew on Exercise 2.1's scientific-notation word problems (Kalma Pak, light-travel-time) as a substitute "application" flavour. If the syllabus ever extends beyond this book, look for pH-scale or decibel-scale material.
- Unit 4: the two garbled Exercise 4.8 items (wheel radii A1=&pi;r&sup2;&minus;6&pi;x+9&pi; style, squared pressers 25 m&sup2;/36 m&sup2;) still need a clean re-scan before use.
- Unit 5: still untested &mdash; Exercise 5.3 items using fraction-form absolute values (e.g. |1&minus;2y|/3 style) and the remaining Exercise 5.4 compound inequalities (#7, #8, #10).
- Unit 7: see the Unit 7 status note above &mdash; several fresh Miscellaneous Exercise 7 MCQs remain (ordered-pair equality, kite-diagonal intersection, minimum-distance-from-axis, trapezium/rhombus diagonal properties).

## Exam-13 summary

Built 2026-07-17. Prioritised the largest confirmed gaps: Unit 1's entire "Application of Real Numbers in Daily Life" section (Exercise 1.3), Unit 2's antilogarithm technique and log-domain/change-of-base identities, Unit 4's "Application of Factorization in Daily Life" section (Exercise 4.8, cubical tank problem), Unit 5's two never-used Exercise 5.4 items (word problem and value-checking), and Unit 7's midpoint-quadrilateral (Varignon parallelogram) problem. Paper structure was also varied from prior exams: Section B offers 14 questions (attempt any 11) and Section C offers 5 questions (attempt any 4), rather than the previous main+OR-alternative pairing, per Atif's specific instruction for this build. Zero verbatim or near-verbatim overlap with exam-01 through exam-04 and exam-10 through exam-12 was confirmed by extracting and cross-checking all prior question text and numeric values before writing new questions.

## Exam-14 (this build) summary

Built 2026-07-28, in `math/exams/exam-14-ch1-2-4-5-7/`. Reverted to the standard main+OR pairing format (Section B: 11 questions, Section C: 4 questions, matching the exam-09/11/12 gold-standard template) per this build's instructions. Sourced content by reading `chapters-ocr/compressed/unit-01, 02, 04, 05` via `pdftotext -layout` (all four have usable text layers) and `unit-07` as rendered page images via `pdftoppm` (its text layer is broken, returns only "CamScanner"). Closed all five gaps flagged at the end of exam-13: (1) six fresh Exercise 1.3 word problems (bank balance, fabric cost/yard, balloons, banner, hiking-club reasonableness, Wajid petrol-average reasonableness); (2) a genuinely different Unit 2 real-world application (Exercise 2.1 scientific-notation word problems) instead of another Richter-scale question; (3) the two remaining Exercise 4.8 daily-life factorization items (veranda, machine surface); (4) a fresh radical equation and set-builder-notation question for Unit 5; (5) both previously-flagged Unit 7 items (Exercise 7.2 Q6 Hassan/Ali race problem, Q7 square/rectangle missing-coordinate labelling), plus a fresh rhombus proof and hypotenuse-length problem from Miscellaneous Exercise 7. Mark distribution (content-mass-proportional, Unit 4 largest): Unit 1 = 12 marks (3 MCQ + 3 short, no Section C slot by design, matching the exam-11/12 precedent), Unit 2 = 13 marks (2 MCQ + 2 short + 1 long), Unit 4 = 14 marks (3 MCQ + 2 short + 1 long), Unit 5 = 13 marks (2 MCQ + 2 short + 1 long), Unit 7 = 13 marks (2 MCQ + 2 short + 1 long); total 65. Zero verbatim or near-verbatim overlap with exam-01 through exam-13 was confirmed by extracting the full text of all 13 prior papers (`pdftotext -layout`) and grep-checking every new question's key numbers/expressions against that combined text before finalising.

## Exam-15 (this build) — 2026-08-18

**Non-standard structure at Atif's request:** 24 MCQs + 3 short (3 marks) + 2 long (5 marks) = **43 marks**, 2 hours, **no OR alternatives**.

**Every question carries an SLO citation**, under the never-out-of-syllabus rule adopted after Physics exam-13. Units 1, 2, 4 and 5 have usable text layers so their SLO lists were read directly; **Unit 7 is image-only** and its SLO page was read as an image.

| Q | Unit | SLO cited |
|---|---|---|
| 1 | U1 | real numbers as union of rationals and irrationals |
| 2 | U1 | concept of radicals and radicands |
| 3 | U1 | transform radical form to exponential form |
| 4 | U1 | terminating and non-terminating recurring decimals |
| 5 | U1 | apply the laws of exponents |
| 6 | U2 | express a number in standard form of scientific notation |
| 7 | U2 | define logarithm of a number to the base a |
| 8 | U2 | characteristic and mantissa |
| 9 | U2 | differentiate common and natural logarithm |
| 10 | U2 | prove and apply the four basic laws of logarithm |
| 11 | U4 | recall factorization of a² − b² |
| 12 | U4 | factorize x² + px + q |
| 13 | U4 | factorize a³ + b³ |
| 14 | U4 | relationship between HCF and LCM |
| 15 | U4 | recall factorization of ka + kb + kc |
| 16 | U4 | recall factorization of a² + 2ab + b² |
| 17 | U5 | define absolute value |
| 18 | U5 | solve linear equation with rational coefficients |
| 19 | U5 | properties of inequalities (trichotomy) |
| 20 | U5 | properties of inequalities (multiplicative), solve inequalities |
| 21 | U7 | distance between points on a coordinate line, d = \|b − a\| |
| 22 | U7 | find distance between two points in the plane |
| 23 | U7 | derive mid-point formula and calculate mid-point |
| 24 | U7 | represent and identify collinear and non-collinear points |

Section B: 2(i) U1 (radical→exponential form, laws of exponents); 2(ii) U2 (laws of logarithms, log₅125); 2(iii) U5 (solve 7x − 4 ≤ 24, naming the property used at each step).
Section C: 3(i) U4 multi-part (x²+9x+20; 8a³+27b³; HCF/LCM of 8a²b and 12ab³ with verification that HCF×LCM = product); 3(ii) U7 multi-part (distance A(−1,2)–B(5,10) = 10; mid-point (2,6); verify AM = MB = 5). Both Section C questions are multi-step per the standing Maths requirement.

**UNIT 10 EXCLUDED** per [[no-geometry-box]] — no practical geometry, no construction questions. Units 3, 6, 8, 9 and 11 are not in the studied scope and were not touched.

**No cross-subject contamination.** Every question comes from the Maths textbook only.

**Uniqueness:** all prior Maths exams (exam-01 to exam-14) were extracted and grep-checked. Favoured the least-used angles (terminating decimals 0 prior hits, exponential form 1, radicand 2, trichotomy 3, natural logarithm 3) over the saturated ones (HCF/LCM 36 hits, mid-point 21, square root 14). Four numeric collisions were caught and changed before finalising: x²+7x+12 → **x²+9x+20**; HCF/LCM of 6x²y and 9xy² → **8a²b and 12ab³**; points (1,2)/(7,10) and (2,4)/(6,8) → **A(−1,2), B(5,10)** and mid-point MCQ **(−3,5),(7,1)**; log₃81 → **log₅125**; 5x−3 → **7x−4**; 3x−6 → **4x−12**.

**All answers independently recomputed** before the key was finalised.

## Exam-15 (this build) — 2026-08-18, attempted 2026-08-19

**Non-standard structure at Atif's request:** 24 MCQs + 3 short (3 marks) + 2 long (5 marks) = **43 marks**, 2 hours, **no OR alternatives**.

**Every question carries an SLO citation**, per the never-out-of-syllabus rule adopted after Physics exam-13. Unit SLO lists were read directly from the chapter scans (Unit 7 has no text layer, so its SLO page was read as an image).

| Q | Unit | SLO cited |
|---|---|---|
| 1-5 | U1 Real Numbers | rationals/irrationals union; radicals and radicands; radical to exponential form; terminating vs non-terminating recurring decimals; laws of exponents |
| 6-10 | U2 Logarithms | standard form; define log to base a; characteristic and mantissa; common vs natural log; four basic laws |
| 11-16 | U4 Factorization | a²−b²; x²+px+q; a³+b³; HCF×LCM relationship; ka+kb+kc; a²+2ab+b² |
| 17-20 | U5 Linear Eq. & Ineq. | define absolute value; solve linear equation; properties of inequalities (trichotomy); multiplicative property |
| 21-24 | U7 Coordinate Geometry | distance on a coordinate line \|b−a\|; distance between two points; mid-point formula; collinear points |

Section B: 2(i) U1 (radical→exponential, laws of exponents); 2(ii) U2 (laws of logarithms, log₅125); 2(iii) U5 (solve inequality + name the properties used).
Section C: 3(i) U4 (x²+9x+20, 8a³+27b³, HCF/LCM of 8a²b and 12ab³ with verification); 3(ii) U7 (distance, mid-point and equidistance for A(−1,2), B(5,10)).

**Unit 10 excluded entirely** (no geometry box, per [[no-geometry-box]]); Units 3, 6, 8, 9 and 11 are outside the studied scope and were not touched.

**Uniqueness:** all prior Maths exams (exam-01 to exam-14) extracted and grep-checked. Six numeric collisions were caught and changed before finalising: x²+7x+12 → x²+9x+20; HCF/LCM pair 6x²y and 9xy² → 8a²b and 12ab³; coordinate pairs (1,2)/(7,10) and (2,4)/(6,8) → (−1,2)/(5,10) and (−3,5)/(7,1); log₃81 → log₅125; 5x−3 → 7x−4; 3x−6 → 4x−12. Favoured the least-used angles (terminating decimals 0 prior hits, exponential form 1, radicand 2) over the saturated ones (HCF/LCM 36 hits, mid-point 21, square root 14).

**Attempted 2026-08-19: 41/43 (95.3%, A+).** MCQ 23/24, Section B 8/9, Section C 10/10. The single MCQ miss was Q13 (chose the a³−b³ form for a³+b³), though she then applied the correct identity in Section C. The other mark went on not naming the properties of inequalities in 2(iii). Her strongest paper in months.

## Exam-16 (this build) — 2026-08-21

**Same 43-mark shape as exam-15:** 24 MCQs + 3 short (3 marks) + 2 long (5 marks) = **43 marks**, 2 hours, **no choices**, header "Revision Test 2026". Files: `math/exams/exam-16-ch1-2-4-5-7/exam.pdf` (2 pp) + `answers.pdf` (6 pp).

**Every question carries an SLO citation** and the answer key prints a **"Source in her textbook"** line under all 24 MCQs, per [[mcq-book-citation]]. Units 1, 2, 4 and 5 have usable text layers and their SLO lists were read directly; **Unit 7 is image-only**, so its 15 pages were OCR'd (`pdftoppm -r 300` + `tesseract`) and its SLO page read as an image.

| Q | Unit | SLO cited |
|---|---|---|
| 1 | U1 | recall base, exponent and **value** |
| 2 | U1 | apply the laws of exponents |
| 3 | U1 | depict real numbers on the number line (√19 between 4 and 5) |
| 4 | U1 | know the properties of real numbers (multiplicative identity) |
| 5 | U1 | **recall the history of numbers** (Babylonian sexagesimal, base 60) |
| 6 | U2 | concept of antilog and use of tables |
| 7 | U2 | define logarithm of a number to the base a (log₇7 = 1) |
| 8 | U2 | apply the laws of logarithm (quotient law) |
| 9 | U2 | scientific notation ↔ **standard notation** |
| 10 | U2 | characteristic and mantissa (characteristic of log 3456) |
| 11 | U4 | factorize **a³ + b³** (27x³ + 64) |
| 12 | U4 | recall factorization of ac + ad + bc + bd |
| 13 | U4 | factorize **a³ + 3a²b + 3ab² + b³** |
| 14 | U4 | recall factorization of a² + 2ab + b² − c² |
| 15 | U4 | recall factorization of a² − b² (two-step, complete factorization) |
| 16 | U4 | factorize ax² + bx + c |
| 17 | U5 | **recall linear equation in one variable** (x² = 4 is non-linear) |
| 18 | U5 | properties of inequalities (**additive**) |
| 19 | U5 | solve linear inequalities with rational coefficients |
| 20 | U5 | reduce equations involving radicals to simple linear form |
| 21 | U7 | conventions for coordinates (**abscissa on the y-axis is zero**) |
| 22 | U7 | conventions for coordinates (**equality of ordered pairs**) |
| 23 | U7 | mid-point formula (AC : BC = 2 : 1) |
| 24 | U7 | distance between two points in the plane |

Section B: 2(i) U1 (laws of exponents; (81)^(3/4); radical → exponential form); 2(ii) U2 (evaluate **log 48** from log 2 and log 3, **naming the law used at each step**); 2(iii) U5 (solve |2z − 3| = 9 **and verify both solutions**).

Section C, both multi-step per the standing Maths requirement: 3(i) U4 three-part chain — factorize **1 + 4x⁴** (the a⁴ + 4b⁴ type, via add-and-subtract 4x²), square root of 49p² − 84pq + 36q² by factorization, and a **÷ of two algebraic fractions** reducing to x/(x − 8). 3(ii) U7 — A(−1,−2), B(−1,4), C(7,4): all three side lengths by the distance formula (6, 8, 10), the converse of Pythagoras to prove a right angle at B, then the mid-point of the hypotenuse M(3,1) shown to satisfy **MA = MB = MC = 5**, i.e. half the hypotenuse.

**UNIT 10 EXCLUDED** per [[no-geometry-box]] — no practical geometry, no construction questions. Units 3, 6, 8, 9 and 11 are outside the studied scope and were not touched.

**Deliberate re-test of exam-15's genuine misses:** Q11 targets the **sum-of-cubes sign** (she chose the a³ − b³ form on exam-15 Q13), and its answer-key explanation spells out both sign patterns side by side. Section B 2(ii) and 2(iii) both explicitly demand something extra beyond the answer (naming the law, verifying the roots), because she lost a mark on exam-15 by not naming the properties of inequalities — the marking notes state that those marks hang on the extra step.

**Uniqueness:** all 15 prior Maths papers were extracted (`pdftotext -layout`) into one file and every candidate number and expression was grep-checked before being set. **Eleven** drafted items were rejected as collisions and replaced: √(3x + 1) = 5 (verbatim in a prior Section B), the distance between (−2,1) and (1,5) (used twice), the x² + 7x + 12 MCQ, x⁴ + x²y² + y⁴, √(9x² + 30x + 25), the "a³ + b³ factorizes to" MCQ stem (that is exam-15 Q13 itself), the distributive-property MCQ (5 prior hits), the √7-irrational MCQ, |4x − 3| = 13, log 7 = 0.8451, and three coordinate pairs that had appeared before. Antilog value 2.6180 and every expression in Section C return zero hits across all 15 prior papers.

**Option audit:** a script confirmed no two options in any question are textually **or numerically** identical — this caught Q20 offering both "18/3" and "6", which was changed to "16/3" before the paper was finalised (exactly the trap that voided Physics exam-13 Q2). Answer letters are balanced at exactly **6 A / 6 B / 6 C / 6 D**, verified against the final option ordering.

## Exam-17 (this build) — 2026-09-07

**Custom 50-mark format at Atif's request, mirroring the OPF Girls College First Term Exam (August 2026):** 10 MCQs (1 mark) + 6 short questions (4 marks each) + 2 long questions (8 marks each) = **50 marks**, 2 hours 15 minutes, **zero optional/OR questions anywhere** — every question compulsory. **Question-paper-only delivery**: per a scope change mid-build, no answer key was produced for this exam; every question was still solved and independently verified (numerically, in a scratch Python session) before being committed to the paper.

Sourced content by reading `chapters-ocr/compressed/unit-01, 02, 04, 05` via `pdftotext -layout` (usable text layers) and `unit-07` as rendered page images via `pdftoppm` (its text layer is broken, returns only "CamScanner"). Read Seemab's actual OPF school paper (`seemab-reports/school/2026-08-first-term-exam/math-paper.pdf`) first for style/difficulty calibration, and the overlap report (`seemab-reports/school/2026-08-first-term-exam/practice-vs-school-overlap-2026-09-07.pdf`) for content priorities.

**Priority items closed (per Atif's brief), all with fresh numbers distinct from the school paper:**
1. "Find the other polynomial given P, HCF and LCM" (Section B 2(iii)) — genuinely new question TYPE for this tracker (previously only tested as an abstract "HCF×LCM=P×Q" MCQ concept, never as a full worked computation). Fresh values: P = x²+2x−24, HCF = x−4, LCM = x³+x²−26x+24 ⇒ Q = x²−5x+4 (school used x²−x−6/(x−3)/x³+11x²+12x−12 — no overlap).
2. Right-angled-triangle proof via distance formula + converse of Pythagoras (Section B 2(vi)) — grounded directly in the book's own worked **Example 4** (points (3,4),(3,1),(8,4)) and Exercise 7.1 Q10 (rectangle ⇒ two right triangles). Fresh points used: A(5,7), B(2,3), C(10,−3), right angle at B (legs 5 and 10, hypotenuse 5√5). Distinct from the school's A(−1,2),B(7,5),C(−2,6) and from exam-16's A(−1,−2),B(−1,4),C(7,4).
3. Sum of three algebraic fractions with factorable quadratic denominators (Section B 2(iv)): 1/(x²−1) + 1/(x²−3x+2) + 1/(x²+3x+2), reducing to 3x²/[(x²−1)(x²−4)]. Fresh denominators (difference-of-squares-based), distinct from the school's consecutive-integer-root pattern (x²−3x+2, x²−4x+3, x²−5x+6).
   Also closed: reduce a product of two algebraic fractions to lowest form (Section C 3(i)(a)): [(x²−25)/(x²+8x+15)]×[(x²+3x)/(x²−3x−10)] = x/(x+2). Fresh factors, distinct from the school's (x³−8)/(x²−4)×(x²+6x+8)/(x²−2x+1).
4. Square root by algebraic division method (Section C 3(i)(b)): 9x⁴−12x³+10x²−4x+1 ⇒ ±(3x²−2x+1). Fresh quartic, distinct from all prior division-method quartics used in exam-03/10/16 and from the school's x²/y²−10x/y+27−10y/x+y²/x².
5. Volume-to-cost cuboidal application (school's Q.4 style) was deliberately SKIPPED per Atif's own guidance, since exam-13 and the school both already used this exact application type.

**Section A MCQs (fresh, spread across all 5 units):** exponent simplification (3⁴×3⁻²÷3⁻³); radical addition (√48+√27); log₅(1/25); log 128 from log 2; x²−14x+49 factorization; HCF of 15a³b² & 20a²b³; |−8|+|3|; compound inequality −3≤2x−1≤5; distance (0,0)–(9,12); mid-point of A(−5,3),B(1,−7). One draft MCQ ("exponential form of ⁵√x³") was caught as a **verbatim duplicate** of an existing MCQ and replaced with the √48+√27 item; another draft ("additive property of inequality: a<b ⇒ a+c<b+c") was caught as a near-verbatim duplicate of exam-16 Q18 and replaced with the |−8|+|3| item. A third draft (HCF of 12x²y³-style monomials) was dropped for being nearly identical to monomial-HCF questions used in at least four prior exams and replaced with 15a³b²/20a²b³.

**Answer-letter distribution:** A=2, B=3, C=3, D=2 (out of 10) — balanced.

**Uniqueness check:** all 16 prior Maths papers (`exam-01` through `exam-16`) were extracted with `pdftotext -layout` into one combined file and every new question's key numbers/expressions/coordinate pairs were grep-checked against it, plus a manual read of the OPF school paper for its exact values. Zero verbatim or near-verbatim overlap remains after the three replacements noted above.

**All 18 answers were independently computed and verified** (Section A distances/logs/factorizations; Section B polynomial-division, right-triangle Pythagoras check, partial-fraction sum, absolute-value/inequality solving; Section C fraction reduction, square-root-by-division expansion check, and the collinearity/mid-point chain for P(1,2), Q(4,6), R(7,10)) before finalising the paper. Every numeric value used in a solution appears in its printed question stem.

**UNIT 10 EXCLUDED** per [[no-geometry-box]]. Units 3, 6, 8, 9 and 11 are outside the studied scope and were not touched.

**Post-build correction (2026-09-07, same day):** Atif independently re-solved all 18 questions and caught two issues before this paper reached Seemab:
1. MCQ4 as originally drafted ("log 128 = ?" with options 0.6020/0.9030/1.2040/1.5050) had **no correct option** — 1.5050 is log 32, not log 128 (= 7×0.3010 = 2.1070). Fixed by keeping the stem and replacing the options with 1.5050 / 1.8060 / 2.4080 / **2.1070 (D, correct)** — all four are now clean multiples of log 2 (5×, 6×, 8×, 7×), keeping the question a genuine test of recognising 128 = 2⁷. Letter balance unchanged (still A=2/B=3/C=3/D=2).
2. Short question 2(v)(a) originally used |3x+1|=13, whose second root (−14/3) is needless fraction-grinding for a "verify both solutions" part. Changed to **|2x+1|=13**, giving clean integer roots x=6 and x=−7 — same technique, cleanly verifiable. Checked against all 16 prior papers: no collision.

Both fixes were re-verified numerically before the paper was re-rendered. `exam.pdf` in `math/exams/exam-17-ch1-2-4-5-7/` reflects the corrected version; no other question, the mark distribution, or the no-choice structure changed.
