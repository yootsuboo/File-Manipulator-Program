# File-Manipulator-Program
Recursion project

File Manipulator というプロジェクトに取り組んでみましょう。以下のコマンドとその機能を提供する file_manipulator.py という Python スクリプトを作成してください。引数の入力が正しいかどうかをチェックするバリデータを必ず記述しましょう。

- reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
- copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
- duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
- replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
