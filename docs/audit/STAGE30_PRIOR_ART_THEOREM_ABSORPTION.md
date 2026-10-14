# Stage 30 — Prior-art theorem absorption audit

## 判定

**中心の連続投資・全純粋SPE排除命題が既存の一つの定理にDIRECTLY ABSORBEDされた証拠は得ていない。新規性PASSも出さない。** Gandal–Shy (2001) とKlimenko (2009) の掲載版全文・全命題条件の照合はUNRESOLVED。旧稿・Abstractを掲載版の代わりにしていない。

提案権による政策遮断、制度による投資誘因の変化、標準化の国際外部性、事前／事後の政策評価差は既存の問題である。最も狭く残る差分は、「独立した二次元連続投資を持つ全私的履歴を企業逸脱で絞った後、提案権集合による終端純粋SPEの排除を証明する」ことである。その非同型性と掲載に値する経済的新規性は別問題である。

対象コミット・ワークフロー・独立数学は同ディレクトリのMATH_AUDITを参照。調査日は2026-10-14。下記の頁・命題番号は**実際に読めた版**について記す。取得した第三者PDFはGitHubへ再配布しない。

## 1. 照合の読み深度

| 研究 | 実際に取得・照合した一次文献 | 限界 |
|---|---|---|
| Gandal & Shy (2001) | 掲載誌DOI・出版社情報。1996年WP12-96全文、Propositions 1–4、特にP2の印刷pp.12–13と表2を視覚確認 | 2001年掲載版全文は取得不可。WPは線形交通費、掲載版への同一視は禁止 |
| Klimenko (2009) | 出版社の本文紹介・著者Georgia Techの掲載情報とPDFリンク | 実際の番号付き命題・証明は未取得 |
| Costinot (2008) | MIT著者サイトの掲載版PDF、JIE75,197–213。P2、L2／4／5、制度・タイミング・Appendix | 読めた対象命題について照合可能 |
| Farrell & Simcoe (2012) | 著者BU公開稿、2011-12-08、P3／4／5／7・脚注22・Appendixの関連箇所 | Wiley掲載版との全差分は未照合 |
| Ruiz (2004) | 著者アップロード全文、2004-02-01、P3／6／9、§2.1.4、Conclusion | 最終掲載版・後続版の書誌は未確定 |
| Farrell & Saloner (1988) | 著者アップロードの掲載情報。Berkeley旧WPのPDFは取得先を確認したが番号付き本文は読めず | 掲載版の番号・証明条件はUNRESOLVED |
| Jensen & Thursby (1996) | NBER WP3870、1991-10全文、Theorems1／3／4／5、対応Appendix | 1996年掲載版の定理番号・変更は未照合 |
| Auriol & Benaïm (2000) | 著者所属機関の掲載版PDF、AER90,550–570、P1／2、T1／2 | 観測した命題は照合可能 |
| Katz & Shapiro (1985) | 著者アップロード掲載版全文、AER75,424–440、P4–9 | 観測した命題は照合可能 |
| Harstad (2005) | 出版社・著者所属機関の書誌、2004年NUPI WP662全文、P2・P10・§5 | QJE掲載版の全差分はUNRESOLVED |
| Romer & Rosenthal (1978) | 著者アップロード掲載版、Public Choice33,27–43、§2の問題(4)、P1（p.33） | 固定提案の縮約対応を検討 |
| Baron & Ferejohn (1989) | 著者アップロード・出版社情報 | 番号付き掲載定理を本監査で再構成できずUNRESOLVED |
| Delaney & Driouchi (2025) | Economic Theory掲載版全文、P1／2とAppendices B／C | 最近の標準化・不可逆選択研究として追加照合 |

## 2. 定理単位の吸収マップ

### 2.1 Gandal–Shy：最優先の未閉鎖項目

**2001年掲載版：UNRESOLVED。** DOI [10.1016/S0022-1996(00)00067-2](https://doi.org/10.1016/S0022-1996(00)00067-2)。[出版社](https://www.sciencedirect.com/science/article/pii/S0022199600000672)。

別行として、[1996年WP12-96](https://ageconsearch.umn.edu/record/275615/files/TEL-AVIV-FSWP-252.pdf) のP1（全外国規格の認容が支配戦略となる条件）、P2（変換費用による世界認容／二国unionと、非加盟国の認容最適反応）、P3（高変換費用の排除）、P4（非対称国・移転制約）を読んだ。

| 既存結果 → 対応 | 必要な変換・制約 | 今回の命題は導けるか | WPに対する判定 |
|---|---|---|---|
| 三国、国内CS＋国内企業世界利益 → 今回と同じ国別帰属 | 認容の変換費用を初期Kに置換するだけでは不十分。価格競争、国別認容、先に政府選択 | 地域連合・非加盟国・厚生外部性は重複。初期連続株式投資やA集合は導入されていない | PARTIALLY ABSORBED |
| P2のunion → 私的二社RS | WPでは加盟政府がunionを好む。今回は私的創業企業と加盟政府の利害が異なる | 私的RSを企業が維持できる全SPE排除は追加の論証が必要 | NOT ABSORBED（読んだWPのP2についてのみ） |

**WPの非吸収は2001年掲載版の新規性確認ではない。** 本ユーザーの別研究リポジトリのsource ledgerも掲載版とWPの需要仕様差を記録しており、同じ著者・題名だから版差を無視する扱いは不適切。

### 2.2 Klimenko (2009)

[DOI](https://doi.org/10.1016/j.jinteco.2008.08.005)、[出版社](https://www.sciencedirect.com/science/article/pii/S0022199608001244)、[著者掲載情報](https://econ.gatech.edu/publications/pub/1491)。

- 照合対象：二国の能動的互換政策、完全競争／不完全競争、国際協定、過大・過小互換性。
- 対応候補：国民厚生に外国への効果が内部化されない点、相互互換化の費用負担、政策による市場競争の変化。
- 必要な変換：K・二属性株式投資・三国提案集合・固定公的強制規格への写像。本文紹介だけでは正当化できない。
- **命題番号・仮定・証明条件：取得できず。判定UNRESOLVED。**
- 「Klimenkoには三国がないから新規」とは判定しない。一般的な二国定理から帰結する可能性は、掲載定理を読んで初めて排除できる。

### 2.3 Costinot (2008)

一次文献：[掲載版PDF](https://economics.mit.edu/sites/default/files/publications/standards_final.pdf)。

| 既存定理 → 変数・制度対応 | 制約・変換 | 今回への含意 | 判定 |
|---|---|---|---|
| L2（p.205、Appendix p.211）の効率互換閾値、P2（p.207）のNT/MR順位 → 社会／国別閾値と制度比較 | 政府が規格を先に決め、企業の二種技術・費用は離散。二国Cournotを今回の三市場と初期stocksに変える必要 | 制度順位の逆転や国際外部性を新発見にできない。A≥2で全私的連続SPEが消える結論は導けない | PARTIALLY ABSORBED |
| L4（p.212）のMR下で複数versionを売らない全SPNE排除 → 今回の全戦略ケース排除 | 可変規格選択と海外販売を固定public motionに置換すると別ゲーム | 「有限の比較でなく全SPNEを削る」という論文構成も既存。今回の特定削減不等式は直接含まれない | PARTIALLY ABSORBED |

最も協調的SPNEで制度を比較する既存の選択基準と、今回のNNN経路・観測済RSの比較を混同しない。

### 2.4 Farrell–Simcoe (2012)

一次文献：[BU著者公開稿](https://people.bu.edu/tsimcoe/documents/published/ConsensusRules.pdf)。掲載DOI [10.1111/j.1756-2171.2012.00164.x](https://doi.org/10.1111/j.1756-2171.2012.00164.x)。

P3／P4（公開稿pp.13–15）は中立主体の介入を持つ消耗戦の均衡・一意性。P5（pp.16–17）は規則別の事前R&D誘因、P7（p.19）は私的・社会的改善誘因の乖離。脚注22（p.15）は二票ルールを明示する。

| 対応・変換 | 結果 |
|---|---|
| 提案者品質q／事前改善 → c,a投資、中立介入 → M | 私的情報・時間・選別・規格選択を捨て、国民厚生と単一既存interfaceを追加しなければ同型でない |
| 二票ルール → r=2 | 同じ「2」だけで一致しない。既存稿では中立タイブレーク・複数提案の操作可能性、今回は提案**資格集合**と一つの固定motion |
| 吸収 | 制度→改善誘因の一般的主張はPARTIALLY ABSORBED。今回の中心全SPE命題は読んだP3–7から直接は得られない。掲載版全差分は未閉鎖 |

### 2.5 Ruiz (2004)

一次文献：[著者公開全文](https://www.researchgate.net/publication/228458259_Mix-and-Match_and_International_Standardization_Policy)。

P3（印刷p.9）は政府認容拒否、P6（p.17）・P9（p.25）は企業の内生的位置選択を許しても拒否と国内独占が残る結果。§2.1.4（p.5）の政策→企業価格の順序と、後半の位置選択を確認した。

対応は「国民厚生」「内生的製品属性」「政府標準化政策」。ただし認容拒否が輸入を排除する制度、二部品のmix-and-match、規格選択／価格・位置の段階を、固定public mandateと先に沈むstocksへ変える必要がある。**PARTIALLY ABSORBED。** 内生的属性を導入したこと自体を新規に数えない。今回の全私的SPE排除はそのまま導けない。最終掲載版の書誌はUNRESOLVED。

### 2.6 Farrell–Saloner (1988)

[掲載版情報・著者公開先](https://www.researchgate.net/publication/24048643_Coordination_Through_Committees_and_Markets)、[Berkeley WP](https://escholarship.org/content/qt08w115vq/qt08w115vq.pdf)。

委員会、不可逆な一方的選択、市場主導、両者のhybridが候補対応。今回も不可逆選択と制度の相互作用だが、特定の既存命題から今回を導く条件を確認できていない。**UNRESOLVED。番号を補っていない。** Abstractの一般的な重複だけを定理吸収の証拠にしない。

### 2.7 Jensen–Thursby (1996)／1991WP

一次文献：[NBER WP3870](https://www.nber.org/papers/w3870.pdf)、[1994年Purdue版の書誌](https://docs.lib.purdue.edu/ciberwp/92/)。

実際に読んだ1991WPではT1（pp.9–10）がR&D競争のSPE、T3／T4（pp.14–15）が規格の事前期待厚生と発見後厚生の違い、T5（p.18）がcontingent標準下のライセンス継続。初期開発→政策評価の時間差に最も近い。

今回の固定stocks損失と、先行稿の確率的発見順・消費可能製品の差は同じ会計式ではない。ただし「事前に良い規格が事後にも良いとは限らない」一般命題は既存。**PARTIALLY ABSORBED（WPで確認した時間差の考え方）。1996掲載版はUNRESOLVED。** 1991WPの番号を1996論文の番号として引用しない。

### 2.8 Auriol–Benaïm (2000)

一次文献：[掲載版、著者所属機関](https://libra.unine.ch/bitstreams/ea35a5ca-1789-4106-bd92-f58d1ec60a98/download)。

P1（p.558）は凸／線形効用で確率1の標準化、P2（p.560）は凹効用で予測可能だが互換性が共存し得る条件。T1／T2は確率過程とODE収束の橋。変数は市場share、更新規則、異質効用であり、今回の企業stocks・国民厚生・有限段階SPEにするにはゲームを置き換えなければならない。**NOT ABSORBED（今回の中心命題について）。** 中央介入と民間標準化の効率差という広い主張には先行性がある。

### 2.9 Katz–Shapiro (1985)

一次文献：[著者アップロード掲載版](https://www.researchgate.net/publication/4723878_Network_Externalities_Competition_and_Compatibility)。

P4（p.432付近）・P5（pp.433–434）の互換coalitionと数量、P6–8（pp.434–435）の私的／社会的互換誘因・移転、P9（p.435）の部分coalitionの過大私的誘因が対応候補。fulfilled-expectations networkを今回の線形H,zに置換し、さらに政府と先行stocksが必要。**PARTIALLY ABSORBED。** 互換グループ・部外企業への効果・効率乖離は既存。公的提案権の全SPE排除をこれらから直ちに導いたとは確認できない。

## 3. 応用名を取り去る親定理監査

| 親結果 → 今回への写像 | 必要な制約／写像の失敗 | 判定 |
|---|---|---|
| Romer–Rosenthal (1978), §2問題(4)とP1 p.33：status quoと可決可能proposal → L/Mと投資依存Δ | setterが選ぶ連続支出と国別status quoを一つの固定motionに制限。事前企業投資・複数独立提案者は導かれない | PARTIALLY ABSORBED：agenda遮断の考え方 |
| Baron–Ferejohn (1989)：議会提案・投票 → A/r | 分配可能なsurplus、継続値と提案権の確率を、固定規格・無移転・一回のselectorへ変換。掲載定理の番号付き検証は未完了 | UNRESOLVED |
| Harstad (2004 WP662), P2 pp.12–13：ルール→先行投資 → 制度下のc,a | 投資が私的project valueを変え、移転・政治的powerが誘因を生む。今回の二企業min・市場外部性・setup参入費用への制約は自動ではない | PARTIALLY ABSORBED |
| Harstad同WP §5 pp.28–30、P10 p.30：無移転、提案者がloserなら投票を遮断、他のwinnerに提案機会があれば投票へ | この文章は今回の固定履歴agenda機構に非常に近い。しかしP10の効率的誘因には外部性なし等の条件があり、今回には市場外部性がある。三社ケース全域符号を仮定として入れれば結論を作り込む | PARTIALLY ABSORBED：最も重要な追加先行研究 |
| Harstad (2005 QJE)の掲載版 | WPとの差分・番号は未照合 | UNRESOLVED |
| 集合論：全二要素集合との交差 → A≥2 | 三国宇宙だけ。経済的S(h)の導出は含まれない | DIRECTLY ABSORBED：初等集合補題 |
| min型stocks＋厳密増加費用：使われない最大値を削る | 政策selectorの単調性と費用差相殺が必要。高a利得微分・三社YES人数までは導けない | PARTIALLY ABSORBED：一般的なweakest-link型削減 |
| 同じfinal allocation、歴史費用がIだけ違う → 事前／事後差=I | 今回はI=φa²。他の終端市場なら同じ恒等式にはならない | DIRECTLY ABSORBED：費用会計の恒等式 |

Harstad一次文献：[2004WP](https://www.files.ethz.ch/isn/27440/662.pdf)、[掲載情報](https://www.gsb.stanford.edu/faculty-research/publications/majority-rules-incentives)。Romer–Rosenthal：[著者アップロード](https://www.researchgate.net/publication/225689856_Political_Resource_Allocation_Controlled_Agendas_and_The_Status_Quo)。Baron–Ferejohn：[出版社](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/bargaining-in-legislatures/2636DB331955032B9421DB0EB25467CC)。

### 親モデルからの最強の短い還元

今回の中心命題は、次の条件命題に還元できる：

1. 私的に維持可能なLの残存履歴には、必ず二政府のYES集合がある。
2. すべてのその集合をAがhitすれば、その履歴はLを維持できない。
3. Aが一政府なら、その補集合ペアが私的SPEを構成できる。

2は既知の有限集合の事実。1と3を今回の市場・費用から導くことが残る。その導出は非自明だが、抽象的には「投資をどう選んでも反対coalitionを安定して作れない」という**条件の確認**である。新しい普遍的agenda theoremを得たという説明は不適切。

全体については **DIRECTLY ABSORBEDを証明したわけではない**。既知の成分を複数列挙しただけで全ゲームの新規性を否定していない。一方、投資の導出を含まない初等集合補題だけで掲載価値を肯定することもできない。

## 4. 近年の同分野・隣接分野

[Delaney–Driouchi (2025), 掲載版PDF](https://link.springer.com/content/pdf/10.1007/s00199-025-01654-4.pdf)、Economic Theory80,1177–1201。P1（pp.1188–1191）・P2（pp.1192–1194）とAppendices B／Cは市場採用とcommittee採用のSPEを、確率的timingと非対称payoffから比較する。

投資の不可逆性と「制度で結果が異なる」は最近も研究されている。今回の有限段階・政府投票・min stocksとは写像が異なり、**PARTIALLY ABSORBED（広い機構）、中心閾値は読んだP1／2からNOT ABSORBED**。最近の関連文献を無視して1980年代の基礎研究だけを越えたとする位置付けは弱い。

## 5. 取得失敗と停止記録

Gandal–Shy：出版社のarticle、abs、pdfft、Elsevier本文APIを試行。掲載版全文を得られず。AgEcon SearchとTel Avivの旧PDFは取得したが、AgEcon版は1996WP、Tel Aviv版は別の旧稿。WPの数式と掲載版の差は未解決のまま固定。

Klimenko：出版社article・Elsevier本文API、著者homepageに実在する `~mk198/klimenko_compatibility_standards.pdf`、HTTPSおよび移行先を試行。旧公式PDFはアクセス不能、新配置候補は404。Abstract・本文紹介から命題番号を推測しない。

その他：Farrell–Saloner掲載版の本文番号、Jensen–Thursby1996掲載版、Harstad2005掲載版の版差を閉鎖していない。アクセス不能を「該当定理なし」と解釈しない。検索クラスはagenda setting、collective-choice investment、hold-up、coalition、fixed motion、weakest-link/min investment、standardization under sunk costs。新たな全網羅サーベイを無期限に継続しない。

## 6. 新規性再キルと最小次行動

現在の証拠で残るのは、**限定された縮約制度とパラメータ領域での全連続純粋投資均衡排除**。これを新発見と断定できる文献証拠はまだ不足。広い貢献説明はPARTIALLY ABSORBED、集合閾値・費用差はDIRECTLY ABSORBED。論文全体の掲載価値NO-GOは、この不確実性だけでなく独立の経済的評価に基づく。

閉鎖のための最小作業はGandal–ShyとKlimenko掲載版の命題・証明条件取得、Harstad§5との明示比較。題名や記号の相違を根拠に新規性PASSへ変えない。取得できなければ投稿を見送り、既存成果をworking paperとして保存する。

**別プロジェクトの提案：NO DEFENSIBLE NEXT QUESTION CERTIFIED。** 将来の面白い拡張をこのNO-GOの救済条件にはしない。
