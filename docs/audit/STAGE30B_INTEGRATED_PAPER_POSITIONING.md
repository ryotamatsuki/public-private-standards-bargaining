# Stage30B — 既存の棚卸しと追加結果を統合した論文の貢献構成

## 判断

著者が提示した①「内生的投資による政策回避の失敗」、②「企業と自国政府の
選好の不一致」、③「提案権による投資均衡集合の変化」は、方向として妥当で
ある。ただし、三つの独立した新規性と数えず、**一つの中核メカニズム**として
まとめる。Stage30Bの全私的均衡分類と、均衡選択を固定しない厚生比較を
加えれば、独立したfull-paperとして再構成する実質的な候補になる。

論文の問いは次が最も自然である。

> 民間企業は事前の技術投資で公的標準化を回避できるか。その回避を排除する
> 制度は、どの条件で社会厚生を改善するか。

掲載価値の最終PASSではない。Stage29原稿のStage30 NO-GOを保存する。
今回の成果の区分は構成・研究位置付けであり、新Stage4AとStage6は未閉鎖。
原始式、原稿、以前の証明、負の診断は変更しない。

## 1. 三本の柱

| 論文の柱 | 経済学者が学ぶこと | 依存する結果 | 主な新規性リスク |
|---|---|---|---|
| 私的投資の安定性と政治的支持の分離 | 民間標準を維持する企業と公的置換を支持する自国政府は一致しない。政治的に民間標準を保護するのは未投資の外部国 | Stage30Bの全私的SPEの条件、下記の選好分離の系 | 企業利益・消費者利益の乖離自体は既知。政治的保護と私的投資の結合に差分が必要 |
| 投資調整による制度効果の相殺ができない | 規制への支持を崩す設計は企業にとって安定ではなく、提案機会の拡大が全民間均衡を排除する | Stage27/30の全域排除、Stage30Bの私的集合の分類 | agendaの交差条件は既知。数値2や「連続」を独立の新機構として売らない |
| 制度の有効性と厚生上の望ましさの分離 | 民間均衡を消す改革が、全旧均衡より弱く良い条件と、最悪均衡を改善する一方で最良均衡を失う条件を区別できる | 公的厚生不変性、私的厚生最大値、K_Wによる全均衡比較 | 定数と集合の最大値の比較自体は自明。内生的な集合と上限を閉じた経済的意味が必要 |

第一・第二の柱が説明する制度効果を、第三の柱が評価する。均衡共存、固定費、
会計恒等式を別々の大発見として足し合わせる構成にしない。

## 2. 選好分離を数値例から全私的均衡の系へ

Stage30Bで、全ての私的純粋SPEの創業企業の利得は `F(c,a)-K`、かつ
`F(c,a)>=P`、`P=pi_I^g-phi/2` と構成されている。同じ投資済み履歴から
公的規格へ移行した場合、その企業の総費用は `K+phi*(1+a^2)/2` なので、
公的利得は `P-K-phi*a^2/2` となる。したがって

\[
 \Delta\pi_{\mathrm{founder}}^{\mathrm{post}}
 =P-F(c,a)-\frac\phi2a^2\le0.                         \tag{S1}
\]

これは新しい独立定理ではなく、Stage30B分類の代数的な系である。
企業は全私的均衡で規格維持を少なくとも弱く選好する。厳密な反対には
`F>P` または `a>0` が必要であり、`F=P,a=0` という参加境界を除外しない。

同じ分類から、全私的均衡で創業国政府の政策利得は `B(c,a)>0`、外部国政府
の政策利得は `V(c,a)-K<0`。政府の利得は企業利得と国内消費者余剰の和なので、

\[
 CS_I-C=B(c,a)-\Delta\pi_{\mathrm{founder}}^{\mathrm{post}}>0.
                                                               \tag{S2}
\]

つまり、創業企業は移行で利益を増やせないが、その国の消費者の便益は損失を
上回り、政府は移行を厳密に支持する。私的な技術参加国と政治的な現状維持の
支持国が異なる。この組合せを投資均衡と制度効果に結び付けることが寄与候補。
ロビー活動、企業と外部政府の共謀、移転契約をモデル化したとは述べない。

数値例の再計算：`eta=.115,K=.55,c=1,a=a_R*≈.398239`で、投資済み履歴
からの移行は、創業企業利益 `-.04974476`、国内消費者余剰 `+.09044836`、
政府厚生 `+.04070360`。著者提示の四捨五入値と一致する。

「選好逆転」は同じ政府が時間の経過で考えを変える結果と混同しやすい。
実際、投資前の公的経路と私的均衡を比べる創業国の厚生差は

\[
 \mathcal W_{I,\mathrm{founder}}^{\mathrm{ante}}
 -\mathcal W_{R,\mathrm{founder}}^{\mathrm{ante}}
 =B(c,a)+\frac\phi2a^2>0.                                \tag{S3}
\]

この政府は投資前も投資後も公的規格を支持する。本文では
**企業と政府の選好の分離／不一致**と呼ぶ方が正確である。世界厚生の事前・
事後逆転と、この主体間の不一致を分ける。

## 3. 政策回避の失敗を説明する直観

「企業が投資できるのに多数決で負ける」だけでは弱い説明である。基準モデル
では、私的に安定な二社設計の共通性投資は `.61` より小さい。一方、既存の
全国厚生証明は少なくとも `a<=.75` で両創業国政府の厳密な公的支持を保証
する。従って、**企業にとって安定な設計集合は、政府の支持を崩す設計の領域
に届かない**。高投資で政策を阻む履歴があっても、それが均衡とは限らない。

二社の設計が不一致なら、互換性に寄与しない余剰投資を削って費用を節約
できる。高い共通設計投資では利益を増やす削減がある。三社の私的投資は、
少なくとも一社に私的開発をやめて公的経路を誘発する逸脱がある。各逸脱が
政府の政策を切り替える場合も含めて、全域で確認する。これが集合論の二政府
閾値と違う実質的な部分である。

この結果は指定された政府の厚生に沿う提案・投票規則と、基準パラメータ
領域についての純粋SPE命題。自由な同時投票の全SPE、混合戦略、任意の公的
実施費用に拡張した主張ではない。

## 4. 厚生を補足結果にとどめない理由

著者提示の⑤～⑦を、最適RSとNNN公的経路の指定比較だけで書くなら、
中心命題を解釈する補足結果という評価が妥当である。Stage30Bの追加結果を
使えば、次の一つの主要成果へ格上げできる。

* 全公的純粋SPEで放棄される共通性投資はゼロで、世界厚生は同一。
* 全私的純粋SPEの中で、`c=1,a=a_R*` が世界厚生を最大化する。
* 可決要件が1票または2票の狭い提案権から、二政府以上へ提案権を拡大する
  とき、全旧純粋SPEより世界厚生が弱く良い必要十分条件は `K<=K_W(eta)`。
* その境界より上では、低厚生の私的均衡と高厚生の私的均衡を同時に排除
  する。最悪の均衡厚生の下限を上げ、達成可能な最大厚生を下げる。

これは期待厚生、現実の均衡選択、各国のPareto改善、無制約の社会的最適
規格の定理ではない。全会一致からの改革を述べるなら可決要件の変更も必要。
全会一致のまま提案権だけを増やしても私的均衡を排除できない。

同じ `eta=.14,K=.55`、同じ狭い提案権制度で、`O(1,0),O(1,0),N` は公的
均衡より世界厚生が `.106147...` 低く、`O(1,.5),O(1,.5),N` は `.048788...`
高い。どちらも私的SPEとして構成されている。この例は「RSなら良い／悪い」
というラベルによる判断ができないことを示す。

## 5. 結果の配置

| 配置 | 残す結果 | 役割 |
|---|---|---|
| 本文の均衡命題 | 全私的均衡の条件、選好分離、公的均衡の放棄投資ゼロ | 何が私的に維持可能か、誰が政策を支持するか |
| 本文の制度命題 | 全域の政策回避失敗、提案権と可決要件の違い | 制度変更がその集合をどう変えるか |
| 本文の厚生命題 | 全均衡の厚生比較、最良・最悪の帰結 | 公的規格への統一の評価 |
| 短い比較静学 | 固定費上昇で私的均衡集合が弱く拡大 | 未投資の外部国への導入費用の帰着。投資量が必ず増えるとは言わない |
| 証明・補足 | 最適aの比較静学、事前・事後会計、Bernstein・根区間、既存の局所頑健性 | 主定理を支える保証と解釈 |
| 限界・診断 | 公的実施費用、自由投票の失敗 | 限定された制度理論である理由。g=Bという固定履歴境界を全SPE分類にしない |

1票可決と2票可決の比較は、証明済みの終局規格の種類・私的集合・厚生集合に
即して記述する。全てのオフパス履歴で政府行動が同じと述べない。七パラメータ
の既存証明が新しい追加命題まで保証するとは未確認なので、移植を宣言しない。

## 6. 親理論との差分と評価の抑制

今回再確認した一次資料：

* Katz–Shapiro (1985) 掲載版の著者アップロード、互換性に関する私的・社会的
  誘因の節、Propositions 6–9。消費者余剰・他社利益を私的企業が内部化しない
  という乖離は既知。企業・自国政府の不一致だけで独立の新規性を主張しない。
  <https://www.researchgate.net/publication/4723878_Network_Externalities_Competition_and_Compatibility>
* Farrell–Simcoeの2011-12-08著者公開稿、Proposition 7。消耗戦型の合意形成
  における私的・社会的な事前品質改善誘因の乖離を分析済み。技術内生化や
  制度と投資の関係一般を新しいとしない。掲載版との全差分は未閉鎖。
  <https://people.bu.edu/tsimcoe/documents/published/ConsensusRules.pdf>
* Harstadの2004年NUPI WP662、§5、Proposition 10。損をする提案者の遮断と、
  他の賛成者への提案機会について既に明記。無移転の効率的投資命題は外部性
  がない条件に依存し、今回の市場外部性を自動で吸収しない。2005年掲載版の
  番号・条件の最終照合は未閉鎖。
  <https://www.files.ethz.ch/isn/27440/662.pdf>
* Grossklags–Christin–Chuang (2008)、§4.2、Result 2。最小投資による複数の
  保護均衡と代替選択肢は既知。Stage30BのCornes–Hartley比較も保存する。
  <https://ra.ethz.ch/CDstore/www2008/www2008.org/papers/xhtml/fp879/fp879-grossklags/fp879-grossklags.html>

残る寄与候補は、これら一般論を越えて、**企業が安定に選べる技術、政府の
公的支持、未投資国の阻止、制度による全私的均衡の消滅、選択を置かない厚生
比較を同一の逐次ゲームで閉じたこと**。一つの親定理への吸収はまだ示されて
いないが、それだけでは優先性・掲載価値のPASSにならない。

著者提示の「①高、②中～高」は、経済的な中心性の優先順位として理解する。
確認済みの学術的新規性の評点としては採らない。Gandal–Shy、Klimenkoの
掲載版については引き続きUNRESOLVED。

## 7. 仮の貢献段落と論文構成

Working title: **Agenda Rights and the Displacement of Private Standards**.

以下は改稿候補の貢献段落であり、原稿への反映・投稿用abstractではない。

> Can firms preserve a private standard by adjusting irreversible compatibility
> investments before public intervention? We study a three-country model with
> national-welfare proposal and voting rules. In a certified parameter region,
> private standards are sustained by firms that weakly prefer preservation even
> though their own governments strictly favor public adoption. Political protection
> instead comes from a noninvesting country that would incur a new development
> cost under the public standard. We characterize all private pure-strategy
> subgame-perfect equilibria and show that extending agenda access eliminates
> them when at most two affirmative votes are required. Investments capable of
> blocking intervention cannot be sustained as unilateral best responses. Public
> equilibria have identical welfare, allowing constitutional comparisons without
> selecting a particular private equilibrium. Reform weakly improves world welfare
> relative to every old equilibrium in one region; outside it, reform raises the
> worst equilibrium welfare while eliminating the best private equilibrium. The
> analysis separates successful public standardization from welfare improvement.

本文の順序：問題と親理論との差分 → 現行モデル・政府規則 → 投資均衡と
選好分離 → 制度による排除 → 全均衡の厚生比較 → 限界。複雑な符号証明は
Appendixへ移すが、原始式と経済的な条件の対応、ケース網羅、逸脱の直観は
本文に残す。新しいモデル・別の社会目的・最適規格設計を追加しない。

## 8. 研究としての終点

現在の成果は、現行モデルでfull-paper再構成を一度実施するに足る核候補。
従来原稿をただ長くする、既知の現象を独立貢献として数える、又は文章の
フレーミングだけでStage30 NO-GOを消すことは勧めない。

最低限の閉鎖は二つ：①追加結果の新Stage4Aで全域・境界・政策切替を再監査、
②掲載版と親理論に対するStage6で実質差分を判定する。既知の協調・外部性・
agenda論の特殊例としか説明できないなら、追加モデルを探さずnoteまたは
working paperへ縮小する。この統合案は新しい無期限探索を承認しない。
