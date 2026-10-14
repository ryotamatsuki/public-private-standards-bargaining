# Stage 30 — Revision Priority and Stop Rule

**Canonical verdict: NO-GO for the current full paper. Stage31 blocked.**

Frozen baseline: PR #57, `2e96112280599cceaee43b89e265fcb5c073f1ca`.
原稿を変更せず、監査証拠を先に固定した。ここにある「修正」は推薦であり、元モデルを改造する作業の開始ではない。

## 優先順位

| ID | 重要度 | 課題・証拠 | 対応の性質 | 最小対応と再監査 | earliest gate |
|---|---|---|---|---|---|
| P0 | FATAL（現在のfull-paperの編集価値） | 数学の全域閉鎖に比べて経済的核が薄い。ECONOMIC_AUDIT §§1–2,7–10／EDITOR §§2–5 | 経済学的主張・記事構成。full-paperの強化は追加研究なしでは解決できない可能性 | 現成果のみのdiagnostic noteへ再構成し、120–200語の寄与説明を一回審査。失敗ならworking paperで停止 | 7.5／11 |
| P1 | MAJOR BUT FIXABLE | Gandal–Shy・Klimenkoの掲載版命題未閉鎖。PRIOR_ART §§2,5 | 先行研究との位置付け | 掲載版の命題・仮定・証明を取得し、今回が短いcorollaryか判定。未取得ならUNRESOLVED継続、投稿しない | 6 |
| P2 | MAJOR BUT FIXABLE（自由投票まで主張する場合はFATAL） | prescribed vote selectorと通常の投票SPEの違い。全NO→NNN-Lという診断2 | 数学的証明の範囲・経済学的主張 | 縮約制度を維持するなら明記のみ。別の投票gameへ変更するなら4/4Aへrollbackし全影響箇所再証明 | 4A／7.5A |
| P3 | MAJOR BUT FIXABLE | public費用・同familyのK再利用・二社／三社需要切替。診断g=.04でRS存続 | 仮定と経済学的主張。根本モデル変更には追加研究が必要 | 制度限定と技術説明を補い、負の診断を残す。修正のため新しい規格選択・費用関数は本枝に追加しない | 7.5A |
| P4 | MAJOR BUT FIXABLE | Harstadの無移転proposal遮断・先行投資が未引用 | 先行研究との位置付け | 2004WP§5/P10と掲載版の版差を明記し、独自部分を連続投資閉鎖に限定する | 6 |
| P5 | MAJOR BUT FIXABLE | 厚生差は会計恒等式、制度の実現順位は未確定 | 経済学的主張／英文 | 「新しい厚生機構」を弱め、二経路と観測済retrofitを固定。最適planner・一意の改革効果と呼ばない | 7／11 |
| P6 | MAJOR BUT FIXABLE（保証水準） | formal gate未閉鎖。七パラメータ証明は再現だが全量独立再生成なし | 数学的保証・provenance | noteを続ける時に必要な対象だけを定めて閉鎖。SymPyをLean PASSに読み替えない。author確認を捏造しない | 7.5A／8 |
| P7 | MINOR | crossed adjugateのQ_iが省略、r=1外部提案者の連続性説明、H/M記号 | 数学的橋・英文構成 | EXPOSITION_REVISIONSの具体案。変更した式・境界だけ再確認 | 10／11 |
| P8 | MINOR | Introduction／robustnessの機構説明の反復、費用のopportunity-cost表現、first/second derivative文言 | 英文・論文構成 | 提示した原文→改稿案で短縮。主張を強めない | 10／13 |
| P9 | MAJOR BUT FIXABLE（量化） | Conclusionのunique public equilibriumは初期行動の一意性まで読める。EXPOSITION_REVISIONSのE10 | 経済学的主張・英文 | unique terminal standard typeへ訂正。主定理は変更せず、この箇所のscopeを再監査 | 7.5A／11 |

P0のFATALは現状の記事種別・掲載価値についての判断。**基準中心定理にFATALな数学的誤りを発見したという意味ではない。** P2も、原稿で明示された縮約規則なら限定修正であり、診断制度の反例を元ゲームの誤りとして隠し持たない。

## 今回採用しない拡張

- 公的規格の内生設計、私的patent・royalty、移転、国数増加、混合投資、最適憲法の新探索。
- 成功するまで需要・費用仕様を替えるportability救済。
- 係数検査個数を増やすだけの強化。
- 期待するジャーナルに合わせた評点引き上げ。

これらは独立の研究問題になり得るが、今回の採録判断に必要不可欠と確認したものではない。

## 限定改稿の受入条件

一回の再構成で以下を全部示せる場合だけ再審査する：

1. 最接近定理から直接吸収されない、読者に新たな理解を与える具体的な寄与。
2. 投票・提案の原始制度と「全SPE」の量化の一致。
3. public fallbackと需要仕様の正直な限定。
4. 事前／事後／国別の厚生比較の整合、制度選択の未解決の明記。
5. ノート本文からAppendixまで専門家が追える証明、変更箇所の再監査、保証の未完了項目の適切な閉鎖。

「数理が正しい」「文献と記号が違う」「もう少し強くできそう」は受入条件ではない。

## Rollbackと証拠固定

- 元のStage29原稿、Stage11–27コード・文書は保持。
- 縮約ゲームの範囲修正なら4A／7.5Aのcertificateを更新。自由投票gameを採る場合は4／4Aから再開。
- 新規性が直接吸収されるなら6へ戻して寄与を削除し、独立の寄与が残らなければ終了。
- g診断は別モデルの失敗。旧中心定理の撤回を要求しない。機構のportability certificateだけMODEL/INSTITUTION-SPECIFICにする。
- 基準定理の具体的反例は発見していないので、不正確な「Stage19/21を全撤回」は勧告しない。
- 古いPASSを黙って編集しない。必要なregression記録はStage30に固定し、著者の選択後に変更管理する。
- Conclusionの一意性表現はMANUSCRIPT QUANTIFIER REGRESSIONとして明示記録した。縮約された主定理の反証ではない。

**投資方針：投稿準備への自動進行を止め、既存成果の短縮・位置付けの修正だけに一度限って投資する。それで掲載理由が立たなければ、この枝を終える。**
