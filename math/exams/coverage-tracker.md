# Math Exam Coverage Tracker

Tracks which sub-topics have been tested in which exam, per [[exam-coverage-discipline]]. Built retroactively on 2026-07-17 while creating exam-13, by reading the full text of exam-01 through exam-04 and exam-10 through exam-12 (via `pdftotext -layout`) and cross-checking every new exam-13 question against that history. Update this file whenever a new math exam is built.

Exam key: 01=Ch1-2 (Real Numbers, Logarithms) | 02=Ch3-5 (Sets & Relations, Factorization, Linear Equations & Inequalities &mdash; Unit 3 Sets is no longer in the confirmed syllabus) | 03=Ch4-5-7 (Factorization, Linear Equations, Coordinate Geometry) | 04=Ch4 (Factorization only) | 10=Ch1-2-4-5-7-10 (comprehensive, includes Practical Geometry which is now excluded) | 11=Ch1-2-4-5-7 | 12=Ch1-2-4-5-7 | 13=Ch1-2-4-5-7 (this build).

**Note:** Unit 3 (Sets & Relations), Unit 6 (Trigonometry), Unit 8 (Geometry of Straight Lines), Unit 9 (Geometry & Polygons), and Unit 11 (Basic Statistics) are outside Seemab's confirmed current syllabus and are not tracked here. **Unit 10 (Practical Geometry) is deliberately excluded from exam-13 and all future exams** because Seemab has no geometry box &mdash; zero construction questions until Atif confirms otherwise.

## Unit 1 &mdash; Real Numbers

| Sub-topic | Tested in |
|---|---|
| Real numbers = union of rational & irrational | 01, 10, 11, 12 |
| Basic properties (closure, commutative, associative, identity, inverse) &mdash; identify/state | 01, 11, 12 |
| Distributive property a(b+c)=ab+ac | 01, 12 |
| Trichotomy property &mdash; verify with given values | 01, **13 (fresh: irrational values a=&minus;2&radic;3, b=&minus;5)** |
| **Properties of equality/inequality as a named "identify the property" short question** (transitive, multiplicative-of-inequality) | **13 (first time explicitly tested this way)** |
| Radicals: product/quotient rule, simplify, reduce index | 01, 11 |
| Laws of exponents (rational & negative exponents) | 01, 11, 12 |
| Scientific notation (MCQ identification & conversions) | 01, 11 |
| Number line representation of inequalities | 01 |
| Additive/multiplicative inverse concepts | 01, 12 |
| **Multiplicative inverse of 0 (no inverse exists)** | **13 (first time)** |
| **Radical &harr; exponential form: denominator of exponent = index of radical** | **13 (first time as MCQ)** |
| TRUE/FALSE rational vs irrational statements with counterexample | 11, 12 |
| **Application of real numbers in daily life** (Exercise 1.3: unit-rate word problem, ratio-sharing of a penalty, Fahrenheit/Kelvin temperature conversion) | **13 (first time &mdash; this was the single biggest Unit 1 gap; Exercise 1.3 had never been drawn from before)** |

## Unit 2 &mdash; Logarithms

| Sub-topic | Tested in |
|---|---|
| Definition of logarithm, exponential &harr; logarithmic form | 01, 10 |
| Characteristic of a logarithm | 01, 10, 12 |
| log<sub>b</sub>1=0, log<sub>b</sub>b=1, base of natural log = e | 01 |
| Laws of logarithms (product, quotient, power) &mdash; expand/combine | 01, 10, 11, 12 |
| Evaluate using given log 2, log 3, log 5(, log 7) values | 01, 10, 11, 12, 13 |
| Digits in a<sup>n</sup> via logs | 01 (2<sup>20</sup>, 5<sup>37</sup>), 11 (3<sup>30</sup>), **13 (fresh: 7<sup>40</sup>)** |
| Richter-scale / earthquake-magnitude word problems | 01 (Pakistan 2005 vs China 1978; Kansu vs Tokyo) &mdash; **heavily recycled, deliberately avoided again in exam-13** |
| Evaluate complex log-table expressions (nth-root combinations) | 11, 12 |
| Scientific notation &harr; standard notation | 01, 10 |
| **Antilogarithm** (find antilog of a given value) | **13 (first time &mdash; a full worked technique in the book that no prior exam had ever asked)** |
| **Domain / definedness of a log expression** (log<sub>2</sub>(7&minus;x) for several x) | **13 (first time)** |
| **"Important results" identities** (log<sub>c</sub>a &middot; log<sub>a</sub>b = log<sub>c</sub>b) | **13 (first time)** |

## Unit 4 &mdash; Factorization & Algebraic Manipulation

| Sub-topic | Tested in |
|---|---|
| Type VI (a<sup>4</sup>+a<sup>2</sup>b<sup>2</sup>+b<sup>4</sup>, a<sup>4</sup>+4b<sup>4</sup>) | 03, 11 |
| Trinomial factorization x<sup>2</sup>+px+q, ax<sup>2</sup>+bx+c | 02, 03, 04, 10, 11, 12, **13 (fresh: x<sup>2</sup>&minus;11x+30)** |
| Type IX (four-binomial products with substitution) | 02, 03, 04, 10, 11, 12 |
| Sum/difference of cubes | 02, 03, 04, 10, 11, 12, **13 (fresh coefficients: 27+512x<sup>3</sup>, a<sup>6</sup>&minus;64)** |
| HCF by factorization | 02, 03, 04, 10, 11, 12, **13 (fresh: 12x<sup>2</sup>+x&minus;1, 15x<sup>2</sup>+8x+1)** |
| HCF by division method | 04 |
| LCM by factorization | 02, 03, 04, 11 |
| Relation LCM&times;HCF = P&times;Q, find missing polynomial | 04, 10, 12 |
| Square root by factorization | 03, 04, 10, 11, **13 (fresh: 25a<sup>4</sup>&minus;30a<sup>3</sup>+9a<sup>2</sup>)** |
| Square root by division method | 03, 10 |
| Simplify algebraic fractions (&times;, &divide;, +, &minus;, DMAS) | 02, 04, 10, 12 |
| **Application of factorization in daily life** (Exercise 4.8: cubical tank volume &rarr; height &rarr; surface area &rarr; painting cost) | **13 (first time &mdash; the entire "Application of Factorization in Daily Life" section, Exercise 4.8, had never been drawn from before)** |
| **Conceptual property: HCF unchanged when polynomials are scaled by a constant** | **13 (first time as MCQ)** |

## Unit 5 &mdash; Linear Equations & Inequalities

| Sub-topic | Tested in |
|---|---|
| Linear equations with fractional coefficients | 02, 10, 11, 12 |
| Linear equations with decimal coefficients | 11, 12 |
| Radical equations &radic;(x+5)=4 style | 02, 11 |
| Absolute value equations \|ax+b\|=c | 02, 03, 10, 11, 12, **13 (fresh: \|5x&minus;3\|=\|x+7\|, \|2y&minus;5\|=9)** |
| Compound inequalities joined by "and"/"or" | 02, 03, 10, 11, 12, **13 (fresh: 5x+10 &lt; &minus;35 or &gt; &minus;5)** |
| Word problems (consecutive integers, bounded ranges) | 03, 12 |
| **Word problem: "two times a number decreased by 5 &ge; number increased by 8"** | **13 (first time &mdash; Exercise 5.4 Q12 had never been used)** |
| **Checking whether a given value satisfies an inequality (verify, don't solve)** | **13 (first time &mdash; Exercise 5.4 Q1(a) had never been used)** |

## Unit 7 &mdash; Coordinate Geometry

| Sub-topic | Tested in |
|---|---|
| Distance formula | 03, 10, 11, 12, **13 (fresh: decimal-input midpoint pairing)** |
| Midpoint formula | 03, 10, 11, 12, **13 (fresh: decimal coordinates (1.4,&minus;1.5) & (2.6,3.5))** |
| Collinearity of three points | 03, 11, 12 |
| Prove vertices form a square / rectangle / parallelogram / rhombus | 03, 10, 11, 12 |
| Distance/midpoint of the hypotenuse of a right triangle | 12 |
| Diameter/centre of a circle from its endpoints | 12 |
| Midsegment theorem (triangle midpoints, DE = &frac12;BC) | 12 |
| **Quadrant identification from point signs** | **13 (first time as MCQ)** |
| **Segment-ratio reasoning at a midpoint (PR = PS &rArr; RS)** | **13 (first time)** |
| **Missing 4th vertex of a rectangle found algebraically (not "prove all 4 given")** | **13 (first time with this framing)** |
| **Midpoint quadrilateral / Varignon parallelogram** (join midpoints of a general quadrilateral, identify the shape formed) | **13 (first time &mdash; Exercise 7.2 Q2 had never been used; this was the biggest Unit 7 gap)** |

## Known remaining gaps (for future exams to prioritise)

- Unit 1: Exercise 1.3's other word problems (bank-balance subtraction, fabric cost-per-yard, unit-rate reasonableness, balloon/banner cost problems) are still untested beyond the two used in exam-13.
- Unit 2: the Richter-scale framing is over-used across exam-01; find a genuinely different real-world log application (e.g. pH scale, sound decibels) if the syllabus ever extends to it, since the book itself only offers Richter-scale and log-table numeric drills.
- Unit 4: Exercise 4.8 still has the veranda-area and machine-surface-area word problems untested (only the cubical-tank one was used in exam-13).
- Unit 5: extraneous-root radical equations remain lightly tested relative to absolute-value equations; consider prioritising radical equations next.
- Unit 7: the "label the missing coordinates of a square OLMN" (Exercise 7.2 Q7(i)) and the Hassan/Ali equidistant race-point problem (Exercise 7.2 Q6) remain untested and are strong candidates for a future paper.

## Exam-13 (this build) summary

Built 2026-07-17. Prioritised the largest confirmed gaps: Unit 1's entire "Application of Real Numbers in Daily Life" section (Exercise 1.3), Unit 2's antilogarithm technique and log-domain/change-of-base identities, Unit 4's "Application of Factorization in Daily Life" section (Exercise 4.8, cubical tank problem), Unit 5's two never-used Exercise 5.4 items (word problem and value-checking), and Unit 7's midpoint-quadrilateral (Varignon parallelogram) problem. Paper structure was also varied from prior exams: Section B offers 14 questions (attempt any 11) and Section C offers 5 questions (attempt any 4), rather than the previous main+OR-alternative pairing, per Atif's specific instruction for this build. Zero verbatim or near-verbatim overlap with exam-01 through exam-04 and exam-10 through exam-12 was confirmed by extracting and cross-checking all prior question text and numeric values before writing new questions.
