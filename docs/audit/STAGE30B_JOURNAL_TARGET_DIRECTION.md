# Stage30B — フルペーパーの目標誌と再構成方向

Date: 2026-10-14 UTC. Input commit:
`8cde13a077fae3c66856c11c519b38172b0bde2d`.

**推奨：Journal of Public Economic Theory（JPET）を第一目標とする。
International Journal of Industrial Organization（IJIO）は条件付きの挑戦枠。
フル論文の代替先はReview of Industrial Organization、次にJournal of Economics。**

これは、現在の成果に対応する原稿を設計するための暫定判断である。
Stage29原稿のStage30 NO-GOを取り消さず、Stage31の投稿準備には進まない。
新Stage4A、Stage6、formal gate等が未閉鎖なので、正式な
`PRIMARY JOURNAL SELECTED — GO TO INTEGRATION` は発行しない。
誌名の選択は投稿許可・採択確率・掲載価値のPASSではない。

## 1. 最新ワークフローの適用

workflow `main`をGitHubで確認したSHAは
`81c37dd95fc93d918138ba9d0da86541d3cc1067`。GovernanceのVersionはv2.9。
pipelineにはpost-v2.9の未リリース記述もあるため、最新stableとmainを同一視
しない。今回の誌選定規則はmainのStage12および該当テンプレートで確認した。

適用資料：

- [GOVERNANCE.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/GOVERNANCE.md)、§2.13。
- [THEORY_PAPER_RESEARCH_PIPELINE.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/THEORY_PAPER_RESEARCH_PIPELINE.md)、Stages8/12/13/14。
- [STAGE_12_JOURNAL_POSITIONING.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/templates/STAGE_12_JOURNAL_POSITIONING.md)。
- [JOURNAL_REQUIREMENTS_CHECKLIST.md](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/checklists/JOURNAL_REQUIREMENTS_CHECKLIST.md)。
- Economic Contribution Completeness、Exposition Streamlining、Reviewer Verifiabilityのチェックリスト。

Stage12の規定は “choose journals based on the actual surviving contribution,
not desired prestige”。貢献・読者・論文形式から
[37候補の母集団](STAGE30B_JOURNAL_CANDIDATE_UNIVERSE.md)を作り、主要8誌を
公式scopeと最近の論文で比較した。先行研究の掲載誌は候補漏れの検査に使い、
その誌への投稿を自動で推奨する根拠にしなかった。

同Stage12はStage7.5AのContribution Robustness CertificateとStage11の
surviving contribution setを入力に要求する。追加結果の正式な証明・優先性
認証がない今回の出力は、**PRE-STAGE12 DIRECTION STUDY**である。
候補比較は完了したが、正式なStage12の通過は未判定とする。

## 2. 売るべき貢献と、その保証範囲

中心の問い：

> 企業は事前の互換性投資で公的標準化を回避できるか。その回避を排除する
> 制度改革は、どの条件で世界厚生を改善するか。

| 寄与 | 根拠 | 現在の保証／一般性 | 最大限許される位置付け |
|---|---|---|---|
| 投資調整を含む全民間純粋SPEの排除 | Stage27/30 | 基準領域・指定政府継続は独立監査済み。MODEL-SPECIFIC / INSTITUTION-SPECIFIC | 政策支持を崩す投資が私的に安定しないという限定された制度効果 |
| 全私的投資均衡の条件、公的均衡の放棄投資ゼロ | Stage30B Results and Proofs | 有理証明と逸脱攻撃による構成。新Stage4A未閉鎖 | 新しい主結果の候補。七パラメータへの移植は未確認 |
| 全私的均衡での企業・自国政府の選好分離 | Integrated Paper Positioning S1–S3 | 前行に依存する系。私的企業の選好は弱い不等号 | 企業利益と消費者便益の一般的乖離ではなく、誰が民間標準を政治的に保護するか |
| 均衡選択なしの制度厚生の必要十分条件 | Stage30B、全私的厚生上限と公的厚生不変性 | 新構成の保証範囲。新Stage4A/6未閉鎖 | 全旧純粋SPEとの世界厚生比較。期待厚生、Pareto改善、第一最適とは異なる |
| 固定費による私的均衡集合の拡大 | Stage30B | 指定矩形の集合包含。効果の広さは限定的 | 短い補助比較静学。選ばれる投資量が必ず増えるとは言わない |

政府が自由に同時投票する全SPEを対象にしていない。公的実施費用ゼロ、
既存の公的規格、無移転、pairwise minimum、対称市場と特定需要への依存を
残す。Stage30の費用追加・自由投票の負の診断は限界として本文に記す。
対称性やパラメータ制限そのものを理由に正しい限定理論を棄却しないが、
誌名に合わせてこれを一般的な投票／標準化定理へ拡大しない。

私の評価では、既存成果を三つの独立した新原理として数える構成は弱い。
**投資の安定性と政治的支持の分離を一つの機構として閉じ、制度が消す
均衡集合の厚生を評価する**構成に実質的なfull-paper候補がある。

## 3. 最近の掲載論文との具体的な比較

下表は誌の掲載様式を判断する証拠であり、各論文の定理吸収監査を完了した
という記録ではない。読んだ深さを明示する。abstractのみの例から、一般性
や必須拡張についてその誌全体の規則を推論しない。

| 証拠ID／誌 | 最近の論文・一次資料 | 読み取り範囲と観察 | 今回の論文にとっての意味（判断） |
|---|---|---|---|
| P1 JPET | Hardt, Hoppe-Wewetzer & Klapper (2025), *Profiting From Regulation: The Effects of Emissions Standards on Abatement R&D*, [10.1111/jpet.70055](https://onlinelibrary.wiley.com/doi/10.1111/jpet.70055) | 掲載全文HTMLのAbstract、§2のモデル、§5の結論、Propositions1–4の証明抜粋を確認。Cournotの生産・投資・規制と厚生を分析する条件付き理論。自前の実証推定はない | 産業組織モデルによる規制の意外な投資効果は対象になる。ただし同論文には補助金の評価もある。「政策を入れた」だけで同等の貢献とは言えない |
| P2 JPET | Odora (2025), *Deliberation and Voting: A Matter of Truth or Taste*, [10.1111/jpet.70013](https://onlinelibrary.wiley.com/doi/10.1111/jpet.70013) | 掲載版abstractと書誌のみ。十分大きい選挙集団で真実の伝達が均衡にならない負の結果をOriginal Articleとして掲載 | 診断的・否定的理論を機械的にnoteへ落とす理由はない。今回の指定投票規則を、同論文の戦略的投票と同一視しない |
| P3 IJIO | Llanes (2024), *Innovation incentives in technical standards*, 93,103046, [掲載ページ](https://www.sciencedirect.com/science/article/pii/S0167718724000018)、[著者所属機関の要約](https://economiayadministracion.uc.cl/publicaciones/innovation-incentives-in-technical-standards/)、[著者書誌](https://gllanes.com/research.html) | 著者所属機関のabstract、publisher検索で取得したIntroduction/節要約。掲載全文・全命題の独立照合は未完了。補完技術の開発、特許プール、価格上限、交渉上の優位を扱う | 事前投資を内生化した標準化だけでは新規性にならない。今回の差分候補は国家厚生に基づく政治的保護と全民間均衡排除・全均衡厚生。追加のStage6優先資料 |
| P4 IJIO | *Standard-setting and the incentives to innovate: Evidence from the IEEE patent policy update*, [10.1016/j.ijindorg.2025.103235](https://www.sciencedirect.com/science/article/pii/S0167718725001018), 104 (2026) | Publisherの書誌・abstractの検索取得。実際のIEEE政策変更と特許を用いた差分推定 | 現実の標準化制度が近年の読者の関心にある。ただし、この一例から理論論文にも実証が必須とは推論しない |
| P5 JEMS | Kim (2026; online2025), *Data Portability and Interoperability Between Digital Platforms*,35,219–232, [10.1111/jems.12643](https://onlinelibrary.wiley.com/doi/full/10.1111/jems.12643) | 掲載全文HTMLのAbstract・Introduction・§2のモデルを確認。§5の責任規則の結果はAbstract/Introductionによる確認で、証明監査は未了 | 条件付きinterop理論は対象。実際のGDPRと実施手段に対応する成果がある点が、現行稿より強い。モデルへデータ漏洩や責任ルールを足す理由にはしない |
| P6 RIO | Chou (2026; online2025), *Asymmetric Compatibility Between Open-Source Software and Proprietary Software*,68,217–242, [10.1007/s11151-025-10034-0](https://link.springer.com/article/10.1007/s11151-025-10034-0) | 掲載版abstract、注、公開Appendix。本文はsubscription previewで、全定理照合は未完了。連続的な一方向互換性と異なる企業目的を分析 | 限定された市場モデルで互換性の理由と消費者・投資帰結を示すfull articleは対象。今回も具体的な経済解釈が必要 |
| P7 Journal of Economics | Buccella, Fanti & Gori (2023), *Strategic product compatibility in network industries*,140,141–168, [10.1007/s00712-023-00834-x](https://link.springer.com/article/10.1007/s00712-023-00834-x) | 掲載全文HTMLのIntroduction、§2のゲーム、§3の均衡・厚生式の抜粋、Conclusionを確認。Online Appendixの全量監査はしていない | 今回の方法・規模に直接近いfull article。民間互換性の内生化・複数均衡自体は既知であり、政府による私的均衡集合の消滅が追加知見でなければ弱い |
| P8 Economics of Governance | Marino (2024), *Political and non-political side activities in an agency framework*,25,111–137, [10.1007/s10101-023-00307-3](https://link.springer.com/article/10.1007/s10101-023-00307-3) | 掲載全文、Introduction、一般関数のhidden-actionモデルと契約・厚生の含意。実証事実で動機付ける純理論 | formal governanceの適合性はある。単に「政府がいる」という類似では弱く、制度が制御する権限・行動を明確にする必要 |
| P9 Economics of Governance | Pernagallo (2025), *Too much science*,26,469–490, [10.1007/s10101-025-00335-1](https://link.springer.com/article/10.1007/s10101-025-00335-1) | 掲載全文HTMLのIntroduction、§2とAppendixの抜粋を確認。情報非対称性による社会的非効率を診断。著者は実証論文ではないと明示 | 診断だけを直ちに不適合とする根拠はない。規制一般に比べ制度・市場の類似は間接的で、掲載基準の低さの証拠ではない |
| P10 IEP | *Multimarket contact, cross-market externalities and platform competition* (2025),71,101133, [10.1016/j.infoecopol.2025.101133](https://www.sciencedirect.com/science/article/pii/S0167624525000071) | Publisher検索でabstract、Highlights、data availabilityを取得。全文命題監査は未完了。二面・複数市場の価格競争の理論 | 実証なしでも具体的なデジタル競争政策の診断が対象。今回の一般的技術標準を、そのままデジタルプラットフォームと呼ぶことはできない |
| P11 IJET | Hu, Masuyama & Mizuno (2026), *Common ownership with downstream firm's voluntary investment*, [10.1111/ijet.70026](https://onlinelibrary.wiley.com/doi/10.1111/ijet.70026) | 掲載版abstractと書誌。自主的投資が所有と厚生の既知の関係を変える。abstractは差別化・価格競争にも頑健と記すが、その証明は未監査 | 条件付きoligopoly投資理論は対象。ただし、その頑健性を今回が備えるとは言えない |
| P12 IJET | Xing & Lee (2026), *Strategic delegation and risk-taking in R&D*,22,183–207, [10.1111/ijet.70015](https://onlinelibrary.wiley.com/doi/10.1111/ijet.70015) | 掲載版abstractと書誌。委任する行動の範囲と投資リスク、Cournot/Bertrand、厚生を比較 | 決定権と投資をつなぐapplied theoryの読者がいる。ただし本稿は価格競争比較や委任選択の定理を持たない |

比較対象を十分に近い一論文へ減らせる場合は、その比較を優先する。P1/P7は
full articleを現行モデルの条件付き理論で作る方向の特に有用な証拠である。
P2/P6/P10/P11/P12について、全理論内容を確認したとは書かない。
掲載パターンは規則・採択保証ではなく、編集判断の観察資料である。

## 4. Journal-fit matrixと順位

一般性がMODEL/INSTITUTION-SPECIFICであることを全誌に共通の入力とする。
「順位が低いから狭いモデルでよい」という推論は採らない。以下のリスクは
私の定性的な編集判断であり、公式の採択率ではない。

| 誌／役割 | Current scope・最近の証拠 | 適合と、実証・問題の完成度 | 最も具体的なdesk/referee objection | 判断 |
|---|---|---|---|---|
| **JPET／第一目標** | 集合的意思決定・投票・外部性・規制・厚生を明示。full articlesを扱い、技法の複雑さに上下限を置かない。P1/P2 | 現行の投資―政策―全均衡厚生の問いに最も直接的。実証や無制約の最適政策が一律の必要条件とは示されない | 「政府は規則で動くのに、新しい公共意思決定の理解が得られるのか。既知のmin型協調に政策outside optionを足しただけではないか」 | 最も有力。ただし現在は投稿相当の認証未了。完全な分類が何を追加するかを最優先で説明 |
| **IJIO／挑戦枠** | 公式学会scopeは理論・実証IOの全域。P3/P4 | 互換性投資と規制の市場帰結は合う。P3があるため、事前投資の内生化を新規性にはできない。実証必須とはしない | 「特許・交渉・public開発費を捨象し、なぜこの自由な公的代替が産業組織上の重要な発見を生むのか」 | Stage6と独立編集審査が明確な追加知見を支持した時だけ一度検討。誌のための拡張はしない |
| JEMS／条件付き挑戦代替 | 企業の競争戦略、組織、applied games。P5 | firm strategyを前面に出すなら可能。原稿の主眼が国家厚生・制度改革なのでJPETより弱い一致 | 「マネジャーが学ぶ戦略は何か。政府selectorの性質を企業戦略の発見と数えていないか」 | IJIOと機械的に連続投稿する枝にはしない。別途、企業読者への理由が立つ場合のみ |
| **RIO／full articleの第一代替** | 幅広いIO、規制等の公共政策。実際の条件で検証できる知見を主に重視し、重要な理論も募集。P6 | 市場と政策の結び付き、条件付き互換性理論は合う。独自推定は必要と断定しないが、現実に対応する決定と観察可能な含意を要する | 「誰が提案でき、どの法的権限で強制する制度か。読み手は小さな数値領域の定理から何を判断できるか」 | 数学的に難しい証明の英語を簡潔にし、国・企業ごとの利害と境界を明示すれば合理的な代替 |
| **Journal of Economics／full articleの第二代替** | 理論・数学を含むmicro/macroeconomics。P7 | 条件付きCournot均衡の分類・厚生分析に直接の掲載例。政策実施を新しくモデル化することは一律要件でない | 「既存の互換性ゲームに政府を載せた計算上の特殊例ではないか。制度を変えたことでどの経済理解が変わったのか」 | 現行モデルの範囲を正確に示すapplied-theory articleの現実的な行先候補。新規性不足を免除する誌ではない |
| IJET／full theoryの追加reserve | 公共・IO・ゲーム・厚生をscopeに含む。P11/P12 | conditional investment theoryが合う。P11/P12はより多くの市場制度比較を含む点も記す | 「投資と制度の既知の関係の修正として、方向・条件の追加が十分に重要か」 | U20が具体的理由で不適合になった場合のreserve。最初から長い巡回投稿列に入れない |
| Economics of Governance／制度説明が立つ場合のreserve | 政府・国際組織・規制、formal theoryも明示。P8/P9 | 診断的理論の余地があるが、実際の議題権・法的authorityの説明が弱い | 「国民厚生を機械的に投票へ変える規則は、どのgovernance問題を説明するのか」 | institutional bridgeを現在の制度資料で示せる場合に再順位付け。単に低い安全先としない |
| IEP／情報産業の接続が立つ場合のreserve | 情報・通信・innovationのpolicy-oriented理論／実証。P10 | デジタル互換性は読者に合うが、モデルに実際のデータ・通信構造があるわけではない | 「なぜこの制度は情報産業に固有の政策判断を変えるのか。一般の技術をdigitalと呼び替えただけではないか」 | 現行成果に具体的対応がない限り自動fallbackにしない |

Scope一次資料のURLとアクセス日は候補母集団文書に保存した。JPETの初期
submission baselineは[要件台帳](STAGE30B_JOURNAL_REQUIREMENTS_LEDGER.md)に保存。

## 5. 有力な別分野誌を第一目標にしない理由

- **JIE**：Gandal–Shy/Klimenko/Costinotが掲載され、国際標準化はscope内。
  ただし現時点の最も強い追加理解は、貿易の新しい効果より、政策介入が
  私的投資均衡集合に与える効果と厚生にある。対称三市場を国と呼ぶことだけ
  を国際経済学の寄与としない。掲載版優先性も未閉鎖である。
- **JIndEcon/RAND**：scope外ではない。Boone–Schuett–Tarantino (2024),
  [*Price Commitments in Standard Setting under Asymmetric Information*](https://onlinelibrary.wiley.com/doi/full/10.1111/joie.12351),
  §§1–2はroyalty設計の情報歪みと実施可能なcapを結ぶ。
  Hovenkamp–Lemus–Turner (2025),
  [*Product Development with Lurking Patentees*](https://onlinelibrary.wiley.com/doi/10.1111/1756-2171.12494),
  §§1–3は技術選択・R&Dを内生化してもhold-upが存続する機構を示す。
  両掲載全文を参照したが、今回の結果への完全な吸収監査は未了。
  今回は公共政策の問いを企業間契約理論へ作り替えず、適合するfield誌を選ぶ。
- **EJPE/Public Choice**：実証がないからではない。政府の戦略空間の制約が
  政治的行動の寄与を限定する。自由投票の全SPE排除と誤読される売り方は
  危険。EJPEの2024年の
  [*Transitive delegation in social networks: Theory and experiment*](https://www.sciencedirect.com/science/article/pii/S0176268024000338)
  のpublisher要約もscreenしたが、それだけで理論単独不可とはしない。
- **Economic Theory/GEB**：前者にはDelaney–Driouchi (2025),
  [*Coordination through Committees and Markets with Option Timing Games*](https://link.springer.com/article/10.1007/s00199-025-01654-4)
  があり、標準化・制度比較はscope内。数学的高度さやモデル特殊性だけで
  排除しない。現在はfield questionへの寄与を示す方が自然で、一般的な
  agenda/coalition/coordination理論を前進させたと認証されてはいない。

## 6. JPETを狙う原稿の形

Working titleを **Agenda Rights and the Displacement of Private Standards**
とし、企業投資と公共経済学の関係がタイトル・abstractで分かるようにする。
「二政府が必要」や「七パラメータ証明」を貢献の最初に置かない。

編集者向けの採録審査理由（原稿案ではなくpositioning statement）：

> 公共介入への賛否は、企業が技術を選ぶ前に固定できない。企業は設計を
> 調整して将来の標準化を避け得るからである。この研究は、民間投資の全ての
> 純粋均衡を政策継続と同時に分類し、企業自身と自国政府の選好が一致しない
> 場合に、未投資国が民間標準の政治的保護を担うことを示す。その保護を
> 議題権の拡大が外すと、政策回避を可能にする安定した投資は残らない。
> 一方、公的結果への統一は厚生改善の保証ではない。私的協調の良い均衡と
> 悪い均衡を同時に消すため、制度改革が全旧均衡を弱く改善する条件と、
> 最悪の厚生を改善して最良の厚生を失う条件が異なる。この識別は、私的に
> 最適な一つの設計を選ぶ従来の経路比較では得られない。限られた制度モデル
> でも、政策成立と経済的望ましさを別々に考える公共経済学の診断になる。

最も強い拒否理由：

> 政府が実際にこの提案・賛否規則に従う根拠が弱く、公的規格の無償の利用
> 可能性が結果を作っているかもしれない。投資の連続性や多数の符号証明は
> 経済的重要性の代替にならない。minimum型協調の多重性、企業と消費者の
> 乖離、agendaの交差条件を一つの例に並べたにすぎないなら、新しい全均衡
> 厚生比較も集合の最大値を計算しただけになる。何を理解し直す必要があるか
> を最も近い定理との比較で示せなければ、JPETでもfull articleの採録理由は
> 成立しない。

この反論への現行成果による答えは、政策fallbackによる企業参加条件と
未投資国の拒否条件が私的に安定な設計集合を共に制約し、その集合を制度
改革がどう失わせるかを閉じたことである。これが既知の親定理から直接
得られるかはStage6で判断する。単に「本文を強く書く」ことで解決しない。

| 本文の順序 | 役割と残す結果 |
|---|---|
| Introduction | 問い、直観、主要な均衡・厚生結果、最接近定理との差分とscopeを早く提示。長い文献羅列を先行させない |
| Model | ゲームの時間、連続戦略、費用、政府規則と精緻化、厚生目的を一か所で説明 |
| Private and public equilibria | 全私的均衡の条件、企業・政府の選好分離、公的均衡の放棄投資ゼロを提示 |
| Agenda access and displacement | 全域の私的均衡排除を前節に接続。二提案者の交差補題は短い制度的系 |
| Welfare of reform | 全均衡比較の鋭い条件、最良・最悪の帰結。同じ制度で低・高厚生RSが共存する例 |
| Discussion / Conclusion | 特定selector・public費用への依存を含む限界。実際の最適政策や自由投票の定理へ拡大しない |

一般的な投資・標準化の研究史を長く再説明せず、本文では政治的保護と
私的な安定性のずれに集中する。固定費の集合比較は短く残し、`a_R*`の微分、
会計恒等式、Bernstein展開・係数リストはAppendix/Supplementへ配置する。
ただし証明の経済的条件、ケース網羅、大域逸脱と政策切替の橋は本文か
明確なAppendix参照で追える状態にする。

本文量の作業目安は通常のfull theory articleとして約20–25ページ＋必要な
Appendix。ただし**編集上の目安であり、JPETの公式上限ではない**。長さを
先に満たすために結果・数値例を足さない。図は投資均衡の条件を説明する
一図と、厚生集合の改革を説明する一図が有力だが、図数のノルマにしない。

制度との接続は「この制度が完全に実在する」という主張を作らない。公開
資料から、既存規格の強制適用、提案権、投資費用の帰着という各対応と
対応しない点を説明する。具体的なEU/ISO等への改革提言は現在の結果では
支持しない。この限定を明示した診断的理論の採録理由を評価する。

## 7. 投稿ラダーと止め方

標準ルートは **JPET → RIO → Journal of Economics**。
第一目標は実際の貢献を最も自然な読者に伝えるために選び、単なるranking
順にしない。IJETは最後のfull-theory reserveであり、全候補へ巡回する
計画ではない。採録可能性が保証された「安全誌」は指定しない。

IJIOへの挑戦は、既存モデルのまま、独立のStage6とeditorial auditが
「標準化における私的投資の安定性を既存のIO理解より前進させる」と具体的
に説明できた場合に限り、JPETより先に一度選択できる。P3との差分が弱ければ
この枝を使わない。JEMSは企業読者への理由が別途成立する時の代替挑戦先。

投稿後の拒否が**誌の読者・scopeの不一致**なら、結果を変えず次の適合誌を
検討する。拒否が**定理の欠陥・新規性不足・経済的重要性不足**なら、同じ
原稿を下へ送って問題を隠さず、該当研究gateへ戻る。full-paperの核が
残らなければ、一つの独立した成果に絞ったnoteまたはworking paperとする。
Economics Letters / Economic Theory Bulletinは、その別形式の候補である。
後者は既知結果のcorollaryを適切でないと明示しており、短縮だけで新規性
不足が解消するわけではない。

## 8. 次の契約と未閉鎖事項

1. **新Stage4A**：新しい全民間分類、公的厚生不変性、厚生最大値、政策
   切替を含む有限逸脱を、構成証明に依存しない経路で監査する。
2. **Stage6**：Gandal–Shy/Klimenkoの掲載版、Harstadの掲載版との条件照合を
   閉じる。今回新たに具体化したP3、P7およびBoone et al. / Hovenkamp et al.
   から、最も強い投資・政策／hold-up親命題を優先して吸収可能性を検査する。
   新しい文献名を足すだけの無期限探索にしない。
3. **Stage7.5/7.5A**：full-paperのeditorial value、MODEL/INSTITUTION-SPECIFIC
   の最大文言、formal-verification適用対象と結果、著者の知的判断の記録を
   閉じる。七パラメータ証明の未独立検証を黙ってPASSにしない。
4. 必要な認証・freezeの後、再構成原稿に新Stage11を実施し、正式なStage12
   を更新する。その結果がGOの時にだけStage13/投稿準備へ進む。

現時点では原稿設計の情報を用意しただけで、原始式、既存原稿、証明コード、
Stage30の判定を変更していない。今回のAIによるsource readingと編集判断は
AI側の調査・解釈であり、著者や外部の人間による新規性認証とは記録しない。

**停止規則**：追加モデルなしの一回の再構成・再認証で、政策fallbackと
投資安定性を結ぶ新知見が先行定理に吸収される、または全均衡厚生の追加が
独立した採録理由にならないと判明したら、full-paper枝を閉じる。好みの誌へ
届きそうだという理由で新しい需要・費用・投票制度を際限なく追加しない。
