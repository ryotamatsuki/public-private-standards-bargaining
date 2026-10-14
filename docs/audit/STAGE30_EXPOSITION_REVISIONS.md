# Stage 30 — Exposition Streamlining and Reviewer Verifiability

以下は修正提案であり、原稿を編集していない。原文は固定コミットの実ファイルから段落ごとに抽出した。新しいモデル・新しい定理を本文へ挿入する提案ではない。政府ルールの明記は既存の縮約制度の範囲を明確にする変更で、自由な投票ゲームを選ぶ場合には別の再導出が必要。

## 段落・節の構造診断

| 節 | 評価 | 優先する修正 |
|---|---|---|
| Introduction | 問いと結果は見つけやすいが、最初の一般論と長い証明予告、著者別文献紹介が重い | 官民利害対立と投資による阻止可能性を先に。関連研究は定理差分中心に統合 |
| Model | 費用と需要の式は明確、初期Nも販売企業である点に注意 | aの技術解釈、二社→三社での需要切替、政府行動指定を明示 |
| Policy | 市場→国別利得の橋が読める | 個別企業利益と政府CSの乖離を短く説明。孤立適合の需要を明示 |
| Equilibrium | 個別投票と初期SPEの違いを正しく区別 | 全順序・min削減・quorum1の外部提案者連続性を短い補題で示す |
| Welfare | 二つの時点を分け、会計は正確 | opportunity costの表現を直し、内生aが何を追加するか限定する |
| Robustness | 十分性と必要性の区別は適切 | 本文の係数ノルム説明をAppendixへ。負の制度診断を一つの限界段落に |
| Conclusion | 新政策の提案は控えめ | unique public equilibriumの量化をterminal typeへ訂正 |
| Appendix A/B | 原始式→多項式の橋は比較的良い | crossed Q_iを表示、first/second derivativeの文言、H/M記号混用を修正 |

原稿の英語を不自然だと一括評価していない。大半は文法的に自然である。優先するのは、同じ機構の反復、必要な経済的意味の欠落、量化・費用時点の誤読可能性である。

## 原文と改善案

### E1. manuscript/sections/01_introduction.tex

Generic opening delays the private/government conflict; identify the investment question immediately.

**Original paragraph**

```tex
A public compatibility standard can benefit consumers and firms by placing products on a common technical interface. Yet agreement about the desirability of compatibility need not produce a common standard. Governments care about the profits of domestic producers as well as the benefits to consumers, and these interests may differ across countries. An additional institutional obstacle is easy to overlook: a proposal cannot pass a vote unless someone with the legal right to place it on the agenda chooses to do so. A standard may have enough supporters to win, but no authorized sponsor willing to introduce it.
```

**Proposed replacement**

The governments of two countries may favor replacing a private regional standard even when its founding firms want to retain it. Whether that majority can act depends on who may introduce the public alternative. We ask whether firms can preserve a regional equilibrium by adjusting their earlier investments when proposal access expands.

### E2. manuscript/sections/01_introduction.tex

Separate the reduced political rule, domain and terminal-outcome quantifier.

**Original paragraph**

```tex
Our first result identifies a sharp constitutional threshold in an explicit region of economic primitives. When one or two affirmative national votes are sufficient, \emph{public standardization is the only pure-strategy subgame-perfect equilibrium terminal outcome if and only if at least two governments hold independent proposal rights}. With a sole proposal holder, the other two countries can sustain a privately developed bilateral standard, and the public standard is also supported by an equilibrium. Unanimity preserves privately developed regional equilibria regardless of how proposal rights are distributed. The threshold thus concerns the set of \emph{equilibrium outcomes}, not the uniqueness of each initial technological choice. The analysis does not rule out mixed-strategy equilibria.
```

**Proposed replacement**

Under a prescribed national proposal and voting rule, we establish a threshold for pure-SPE terminal outcomes on an explicit parameter region. When one or two affirmative votes suffice, a public interface is the only terminal standard type in every pure SPE if and only if at least two governments may independently propose it. A sole outsider proposer and unanimity can sustain bilateral regional equilibria. The result covers all legal continuous private investments; it does not identify a unique initial investment vector.

### E3. manuscript/sections/01_introduction.tex

Keep the proof idea; move the long case description to the equilibrium section.

**Original paragraph**

```tex
Why does this institutional threshold extend beyond voting over an assumed private standard? In a three-country polity, any two authorized proposers intersect every two-government majority. The observation is elementary. But an arbitrary private technology profile need not yield two favorable votes. Some heterogeneous private standards can indeed make particular governments oppose a public interface. Our central equilibrium task is therefore to rule out private investment profiles that would both evade the public vote \emph{and} survive a firm's incentive to deviate. With two developers, excessive unilateral compatibility or commonality capital can be reduced without changing the common pair technology; at higher commonality choices, a smaller design adjustment raises private profit while leaving political nonintervention intact. With three developers, surviving private profiles must have ties in their maximal design attributes; careful analysis of the remaining asymmetric cases shows that two national governments weakly support the public mandate. Only after these private-investment restrictions are established does the institutional majority-intersection argument complete the result. Our equilibrium claim is consequently stronger than an ex-post vote calculation at a symmetric regional benchmark.
```

**Proposed replacement**

The set-intersection argument behind this threshold is elementary: any two proposal holders intersect every two-country majority. The substantive equilibrium step is to show that firms cannot sustain a no-intervention design with insufficient effective political support. Redundant investment reductions and global payoff inequalities establish this step for heterogeneous two- and three-developer histories.

### E4. manuscript/sections/02_model.tex

Give the commercial meaning of a rather than an unexplained engineering label.

**Original paragraph**

```tex
At date 1, firms simultaneously choose either \(N\), which entails no private development, or an open design
\begin{equation}
 O(c_i,a_i),\qquad 0\leq a_i\leq c_i\leq 1.
 \label{eq:action}
\end{equation}
The first attribute, \(c_i\), determines the potential compatibility-related demand benefit; \(a_i\) measures common design investment that changes the intensity of competition with compatible and noncompatible producers. They are real physical stocks rather than freely reversible announcements. An initial open developer spends
\begin{equation}
 I(c_i,a_i)=K+\frac{\phi}{2}(c_i^2+a_i^2),
 \qquad K>0,\quad \phi>0.
 \label{eq:initial-investment}
\end{equation}
A firm choosing \(N\) spends nothing. The investment is sunk before any regulatory vote. The feasible triangle \(a_i\leq c_i\) prevents a firm from choosing more commonality than compatibility capacity.
```

**Proposed replacement**

Compatibility capacity determines the demand benefit that a compatible pair can obtain. The second attribute is a design stock that changes product substitution: it makes products within a two-firm cohort closer substitutes while separating that cohort from the remaining producer. These effects are assumed reduced-form demand primitives. The restriction that design commonality cannot exceed compatibility capacity defines the feasible investment triangle.

### E5. manuscript/sections/02_model.tex

A substantive institutional clarification, not a change secretly made to the manuscript.

**Original paragraph**

```tex
At date 2, governments observe the entire vector of initial technology choices. A constitution consists of a nonempty \emph{agenda set} \(\calA\subseteq\{1,2,3\}\) and a \emph{YES quorum} \(r\in\{1,2,3\}\). Every government in \(\calA\) may independently introduce the legally available public mandate; a mandate passes if at least \(r\) governments vote YES. A government always proposes an implementable mandate if it weakly gains from doing so, and votes YES when its national welfare under the mandate weakly exceeds the status quo. These tie rules are maintained throughout. Since the possibility of enactment is common knowledge, this deterministic continuation may be represented by a sequence of individually available public motions and national votes; the legal proposal right does not confer bargaining power over the technical content.
```

**Proposed replacement**

After observing private investments, the institution applies a prescribed proposal and voting rule. A government supports the fixed public motion when its national welfare gain is nonnegative, and an eligible supporter introduces it whenever it can pass. The mandate is enacted exactly when the number of supporters meets the quorum and at least one supporter has proposal eligibility. Firms anticipate this continuation rule when choosing investments. Our pure-SPE statements refer to this reduced game; unrestricted simultaneous voting can support additional continuations.

### E6. manuscript/sections/03_policy.tex

Explain incidence before repeating certificate terminology.

**Original paragraph**

```tex
At this observed optimal regional standard, the national policy gains take the form
\begin{equation}
 (\Delta_1,\Delta_2,\Delta_3)
 =\left(B(\eta),B(\eta),K_V(\eta)-K\right),
 \label{eq:bilateral-votes}
\end{equation}
where
\begin{align}
 B(\eta)
 &=W_I-\frac{\phi}{2}a_R^*(\eta)^2
       -f(a_R^*,\eta)-C_R(a_R^*,\eta),
       \label{eq:B}\\
 K_V(\eta)
 &=W_I-\pi_O(a_R^*,\eta)-C_R(a_R^*,\eta).
       \label{eq:KV}
\end{align}
The two founders' governments strictly prefer the public mandate, \(B(\eta)>0\), while the excluded government's gain \(K_V(\eta)-K\) is strictly negative on (\ref{eq:baseline-box}). The underlying inequalities are certified uniformly over the entire privately optimal design enclosure, not inferred from a single numerical illustration. They deliver exactly two favorable governments. Whether that majority can translate its preferences into policy depends on the proposal entitlement set.
```

**Proposed replacement**

At the privately optimal regional design, both founding governments gain from a public mandate even though each founding firm earns more from retaining the private standard. Consumer benefits account for that divergence. The outsider government instead loses because its domestic firm must incur new setup and compatibility costs. The signs are uniform over the stated optimal-design enclosure. Proposal eligibility determines whether these national preferences can lead to enactment.

### E7. manuscript/sections/04_equilibrium.tex

State the exact object and avoid repeated warnings elsewhere.

**Original paragraph**

```tex
None of this implies that a broader agenda is
world-welfare improving. With unanimity or narrow
agenda control, RS and IS equilibria coexist; a
constitutional comparison must account for the
initial sunk investments supporting each.
The relevant welfare question is not just whether
a mandate would be attractive after a regional
standard has already been installed.
```

**Proposed replacement**

A wider agenda eliminates private regional terminal equilibria on this parameter region. This is an equilibrium-set result, not a welfare ranking of constitutions. Under a narrower agenda, both regional and public paths can be equilibria; the welfare comparison below therefore ranks specified paths and does not assume a unique realized outcome.

### E8. manuscript/sections/05_welfare.tex

Do not describe sunk expenditure as a new opportunity cost of the retrofit.

**Original paragraph**

```tex
The distinction is economically transparent. A privately developed regional standard uses the commonality stock \(a_R^*>0\) to separate a compatible insider pair from a third producer. If the public standard is chosen at the outset, none of that commonality capital needs to be built. If the government instead imposes it after the region has developed the alternative design, the same expenditure has already been made and cannot be recovered. The public outcome then requires firms to abandon the attribute that generated the regional differentiation advantage. The opportunity cost of that abandoned design is
\(\phi(\aR)^2\) across the two regional founders. The two world-welfare comparisons differ by exactly that amount.
```

**Proposed replacement**

The commonality expenditure is already sunk in both alternatives considered after regional investment, so it cancels from that policy comparison. It is incurred only along the regional initial investment path. The ex-ante and ex-post cutoffs therefore differ by the two founders' historical commonality costs. Endogenous design choice determines the size of this wedge, not the accounting reason that it is positive.

### E9. manuscript/sections/06_robustness.tex

Replace a long computational explanation in the main text with the licensed scope; preserve the details in Appendix.

**Original paragraph**

```tex
Adding \(v\) and \(\gamma_0\) introduces a complication:
some three-developer Bernstein coefficients are exactly zero
at the boundary where all relevant private technologies
coincide with \(O(1,0)\).
Strictly positive coefficients are stable under small perturbations,
but zero coefficients require a separate argument.
The relevant boundary welfare numerators vanish identically
for \emph{all} \(v,\gamma_0\), not merely at their baseline values.
After clearing the strictly positive public-technology denominator,
every other coefficient has a rational lower bound above \(1/50\).
An explicit power-basis coefficient-norm estimate bounds
its joint \(v,\gamma_0\) perturbation below \(0.013\)
on the stated narrow intervals.
Hence none of the nonzero coefficients changes sign,
and all structural zeros remain zeros.
Appendix~\ref{app:certificates} states the algebraic objects,
normalizations, and scripts corresponding to these assertions.
The appendix is part of the proof, not an invitation to
accept a finite numerical parameter grid as sufficient.
```

**Proposed replacement**

The additional neighborhood changes primitives within the same demand and political model. Its proof preserves positive coefficient margins and verifies that the zero faces remain structural identities. This establishes local sufficiency, not a necessary-and-sufficient classification or robustness across public-cost and voting institutions. The exact coefficient bounds belong in Appendix B.

### E10. manuscript/sections/07_conclusion.tex

MAJOR quantifier correction: the source says unique public equilibrium, although only terminal standard types are unique.

**Original paragraph**

```tex
The same institutional reform has no unconditional efficiency ranking. The nonmember's national veto, the world-welfare effect of retrofitting after private expenditure is sunk, and the welfare ranking of alternative initial public and private investment paths have three distinct cutoffs. Their ordered difference shows why desirable public standardization at the outset can coexist with an undesirable retrofit after private investment. A rule that produces a unique public equilibrium can also remove a privately developed equilibrium with higher ex-ante world welfare.
```

**Proposed replacement**

The institutional result does not provide an unconditional efficiency ranking. A nonmember's vote, a retrofit of an installed regional standard, and a comparison of two initial investment paths involve different thresholds. Wider proposal access can remove a feasible regional equilibrium that has higher ex-ante welfare than the NNN-to-public path. Without an equilibrium-selection rule, this does not identify the realized welfare effect of reform.

### E11. manuscript/appendix/A_proofs.tex

The source refers to a second derivative expression immediately after displaying the first derivative of F with respect to c.

**Original paragraph**

```tex
Consider two identical open founders \(O(c,a)\) and an undeveloped outsider. Write
\[
 b=\gamma_0+\kappa a-vc,\quad d=\gamma_0-\eta a,
 \quad z=1+\rho c,\quad D=2m(2m+b)-2d^2.
\]
The two symmetric insider quantities \(x\) and the outsider quantity \(y\) solve
\[
 \begin{bmatrix}2m+b&d\\ 2d&2m\end{bmatrix}
 \begin{bmatrix}x\\y\end{bmatrix}
 =
 \begin{bmatrix}z\\1\end{bmatrix}.
\]
Inverting the matrix gives
\begin{equation}
 x=\frac{2mz-d}{D},\qquad
 y=\frac{2m+b-2dz}{D},\qquad D>0.
 \label{eq:app-xy}
\end{equation}
The gross net-of-stock-but-pre-setup profit of a founder is
\[
 F(c,a;\eta)=3m x(c,a,\eta)^2-\frac{\phi}{2}(c^2+a^2).
\]
At fixed \(a\) we have the exact comparative-static identity
\[
 \frac{\partial x}{\partial c}
 =\frac{2m(\rho+vx)}{D}>0,
\quad
 \frac{\partial F}{\partial c}
 =6m x\frac{\partial x}{\partial c}-\phi c.
\]
The second derivative expression alone does not establish a global optimum. A uniform rational inequality uses a conservative positive lower bound on \(x\,\partial x/\partial c\) and confirms \(\partial F/\partial c>0\) on the full feasible triangle for \(\eta\in[.10,.14]\); hence the optimal pair design has \(c=1\).
```

**Proposed replacement**

The sign of the first derivative must be established uniformly before the compatibility boundary can be declared globally optimal. The rational lower-bound argument verifies this sign over the full feasible triangle.

## 文献段落の追加方針

Harstadの無移転proposal遮断と事前投資を位置付けに加える。ただし2004WPの命題を2005掲載版として引用しない。掲載版比較を閉じてからbibliographyを修正する。IntroductionとRobustnessで同じ九研究を二度順番に紹介せず、最接近の三つの問い（国際認容・制度下の投資・全SPEの閉鎖）にまとめる。

## Appendixへの具体的な橋

crossedケースでp=H12、r_c=H13、b=H23、z2=z3を定義した後、次を表示すればproduction codeを開かずに証明対象が追える：

```tex
Q_1=(4m^2-b^2)z_1+(r_c b-2mp)z_2+(pb-2mr_c)z_3,
Q_2=(r_c b-2mp)z_1+(4m^2-r_c^2)z_2+(pr_c-2mb)z_3,
Q_3=(pb-2mr_c)z_1+(pr_c-2mb)z_2+(4m^2-p^2)z_3.
2D_C^2 CS=m\sum_i Q_i^2+
  2(pQ_1Q_2+r_cQ_1Q_3+bQ_2Q_3).
```

これは全Cournot行列の余因子であり、新命題ではない。

quorum1の高a逸脱の補足案：

> If the outsider is entitled to propose and a one-vote quorum applies, an initial L outcome implies that its policy gain is strictly negative. Continuity preserves that negative gain after a sufficiently small reduction in commonality. If the outsider is not entitled, its vote cannot introduce the motion. For a two-vote quorum, one favorable outsider alone cannot enact the mandate when both founders strictly oppose it.

## 量化の回帰記録

Conclusionの “a unique public equilibrium” はStage29のverifiability mapが明示する “not unique initial choices” と合わない。**MANUSCRIPT QUANTIFIER REGRESSION / MAJOR BUT FIXABLE** としてStage7.5A/11へ記録する。終端型の一意性へ直せば、中心定理を変更せずに修復できる。

## 本文の短縮順序

1. 重複するIntroduction／Robustnessの機構・literature説明を統合。
2. 制度規則・主定理・短い直観・一つの厚生経路比較を本文に残す。
3. 全ケース証明と係数計算をAppendixへ置き、前提・証明対象・符号含意は本文から見えるようにする。
4. 資料の取得失敗、CI履歴、author accountabilityは監査資料で保持し、完成論文の主要段落に繰り返さない。

文章の短縮で経済的貢献を増やしたことにはしない。変更を採用する場合には一回の統合コンパイル・引用・label確認と、変更した量化・証明橋の再監査を行う。
