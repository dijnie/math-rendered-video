# Điều phối: lead, các builder và vòng review

File này mô tả cách một lead (người dẫn dắt) đạo diễn một bộ phim mà các shot do agent khác dựng: ai quyết định, ai dựng, mỗi bên được sửa file nào, và công việc được giao brief, review rồi trả lại như thế nào. Nó khái quát những gì hai bộ phim đã dạy, mỗi phim do một lead làm cùng chín builder (người dựng).

Nạp file này khi: bạn là lead và sắp viết authoring guide (hướng dẫn soạn), giao brief cho một builder, review thứ một builder đã dựng, làm lại một shot mà chủ phim đã xem, hoặc quyết định khởi động bao nhiêu builder.

## Thuật ngữ dùng trong file này

| Thuật ngữ | Nghĩa |
|---|---|
| Contact sheet | Một lần chụp chứa nhiều khoảnh khắc của một đoạn, xếp thành lưới, mỗi ô ghi thời điểm của nó |
| Cut sheet | Một contact sheet chứa vài frame trước và sau mỗi chỗ cắt |
| Placeholder card (thẻ giữ chỗ) | Thứ studio phát cho một shot chưa có module: một thẻ nói shot đó sẽ là gì và nháy theo nhạc |
| Plate (nền chữ) | Một mảng nền đặc do overlay chung đặt, trên đó một câu chữ đứng được trên mọi hình |
| Shot data (dữ liệu shot) | Các file liệt kê shot, bar của chúng, chuyển động camera, transition và lời chữ. Tài liệu storyboard, thời điểm shot và placeholder card được sinh ra từ chúng |
| Transition lead, transition tail | Số beat mà một transition chiếm ở cuối shot đi ra, và ở đầu shot đi vào. "Lead" khi không kèm chữ "transition" luôn chỉ vai trò |
| In-world transition (transition trong thế giới) | Một transition diễn ra bên trong thế giới của hai shot, nên builder của chúng tham gia vào nó |

## Vai trò

| Vai trò | Quyết định | Dựng | Không bao giờ |
|---|---|---|---|
| Chủ phim (owner) | Chủ đề, khán giả, thông điệp, độ dài, khung hình, nơi phim được chiếu, ngôn ngữ, hình thức bàn giao. Nhạc, bằng tai. Nội dung và từng câu chữ. Look (diện mạo), trên một mẫu đã dựng. Phim có được chấp nhận hay không. Các quy tắc của máy | Không gì cả | Không bao giờ bị yêu cầu duyệt qua mô tả thứ có thể cho xem hoặc cho nghe. Không bao giờ bị hỏi để chốt điều lead tự tra cứu hoặc tự thử được |
| Lead | Lộ trình, treatment, storyboard, shot data, các quy tắc trong authoring guide, cái gì trả lại cho builder, cái gì được chấp nhận, hình nào được giữ lại qua một lần làm lại | Engine, bộ kit chung, các transition, overlay, studio, công cụ chụp, shot data và bộ sinh của nó, authoring guide, các brief | Dựng một shot, kể cả một mẫu. Bắt đầu công việc mã hoá nội dung hoặc look trước khi chủ phim cho phép. Tiêu tiền hoặc chạy một job nặng mà không hỏi. Trả lời một báo lỗi bằng phỏng đoán |
| Builder | Cách các shot của mình được làm: phương tiện, bố cục, chi tiết camera. Có thể đề xuất thay đổi storyboard, cách một câu chữ đến với người xem và một transition | Các shot trong section của mình, các part file của section đó, ảnh chụp của mình, báo cáo của mình | Sửa engine, bộ kit chung, shot data hoặc file của builder khác. Chép code kit vào file của mình để sửa. Sửa một câu chữ đã duyệt. Mở trình duyệt, server hoặc renderer. Dừng một tiến trình không phải do mình mở. Xuất video |
| Story writer (người viết truyện) | Không gì một mình. Nó suy nghĩ thấu một section hoặc cả phim và viết nháp: các so sánh, ranh giới, các shot của storyboard | Một bản nháp shot data và các câu chữ, kèm lý do và những gì nó chưa chắc | Ghi thẳng vào shot data. Coi bản nháp của mình là đã duyệt. Dựng shot |
| Researcher (người nghiên cứu) | Không gì cả. Nó xác lập sự thật | Một báo cáo có nguồn: một tác phẩm tham chiếu làm gì, một công cụ hoặc dịch vụ làm gì, máy có cài gì | Sửa file dự án. Khẳng định như sự thật điều nó chỉ đọc trong tài liệu. Quyết định thay lead |

Ba quy tắc giữ các vai trò tách bạch.

1. Lead hỏi chủ phim về những gì thuộc về chủ phim, và tự chốt những gì tra cứu hoặc thử được.
2. Chỉ đạo cho builder nêu ý định và để ngỏ phương tiện. Builder nào tìm ra cách tốt hơn để thể hiện cùng một điều thì dùng cách đó và nói rõ trong báo cáo. Điều nó muốn đổi ngoài file của mình thì nó đề xuất.
3. Báo cáo của researcher tách bạch điều tài liệu nói với điều code hoặc dịch vụ thật sự làm. Lead kiểm tra các con số quan trọng bằng một lệnh trực tiếp trước khi dựa vào chúng.

Từ thực tế: một researcher báo engine của một tác phẩm tham chiếu có 2.424 dòng, còn lead tự đếm được 2.260. Tài liệu của một dịch vụ nhạc bỏ ngỏ câu trả lời của nó trông thế nào và độ dài yêu cầu có được giữ không. Một request thật đã giải quyết cả hai.

## Vì sao lead không dựng shot

| Lý do | Điều gì hỏng khi lead dựng |
|---|---|
| Phải có người nhìn cả bộ phim | Lead đang chìm trong một shot thì không nhìn các chỗ cắt, thứ tự, bộ kit hay nội dung, và không ai khác nhìn được |
| Builder đánh giá tốt shot của mình nhưng không thấy được cả phim | Sự chú ý của lead bị dồn vào chỗ builder làm cũng tốt như vậy, và thiếu ở chỗ không builder nào làm được |
| Chủ phim có thể đã cố ý chọn model cho builder | Một shot do lead dựng che mất những gì builder làm được |
| Một hình do lead làm mang sức nặng của một quy tắc | Builder coi nó là chuẩn, và lỗi của nó lan vào công việc của họ |

Quy tắc này không có ngoại lệ cho một mẫu. Nếu đã có phác thảo của lead, hãy giao chúng cho builder của section đó, chỉ rõ điểm yếu, và ghi trong guide rằng chúng chỉ minh hoạ cách dùng kit chứ không phải là chuẩn. Builder có thể giữ, cải thiện hoặc thay chúng.

Từ thực tế: lead bắt đầu viết các shot của section mẫu. Chủ phim chặn lại: "Bạn đang dựng cảnh à? Chỉ quyết định những điều quan trọng thôi, để Opus dựng." Ba bản phác thảo được giao cho builder của section đó kèm điểm yếu đã nêu tên. Một phác thảo chứa bốn ví dụ về một lỗi, và ba trong số đó trông không giống lỗi. Builder giữ các ví dụ, và chủ phim phát hiện ra sai sót sau đó.

## Những gì chỉ lead kiểm tra được

| Cái gì | Bằng cách nào | Nó tìm ra gì |
|---|---|---|
| Các chỗ cắt giữa các section | Một cut sheet của cả phim, và một sheet qua mỗi ranh giới section với shot của cả hai bên đã được nạp | Một shot mở đầu bằng frame trống, một transition bị gãy, một chỗ cắt mà builder không kiểm tra được vì shot bên cạnh chưa tồn tại |
| Cả bộ phim | Một overview sheet: vài chục frame rải đều trên cả phim | Đường cong của màu sắc và nhịp độ, một section lệch thiết kế |
| Bộ kit chung | Xem ảnh chụp từ nhiều section. Đọc code không tìm ra những lỗi này | Một lỗi xuất hiện ở mọi section: chữ bị phát sáng, một bộ đếm in hai giá trị cùng lúc |
| Các giá trị xuất hiện ở nhiều section | So sánh chúng giữa các section và với nguồn duy nhất | Các con số không khớp nhau |
| Chuyển động camera và transition theo thứ tự | Kiểm tra của bộ sinh, rồi đọc danh sách bằng mắt | Hai shot liền nhau chuyển động giống nhau hoặc vào giống nhau |
| Ví dụ và đạo cụ giữa các section | Bảng nội dung (xem `quality-gates.md`) | Hai section dùng chung một ví dụ, một đạo cụ hoặc một kiểu màn hình. Một shot đọc ra như ý tưởng của section khác |
| Tính liên tục giữa các shot kề nhau | Trả lời câu hỏi của builder từ storyboard và từ báo cáo của bên cạnh | Hai section gọi tên một thứ khác nhau, hoặc không thống nhất về những gì đã được vẽ tại chỗ cắt |

Từ thực tế: ở phim đầu, mọi builder đều đánh giá tốt section của mình. Cut sheet của cả phim cho thấy phần lớn các section mở đầu bằng một frame gần như trống, trong đó có cả cú kick đầu tiên của phim. Builder ở cả hai phim đều ghi trong báo cáo rằng chỗ cắt sang section bên cạnh chưa được kiểm tra, vì file của bên cạnh chưa tồn tại lúc họ chụp.

## Quyền sở hữu file

| File | Chủ sở hữu | Builder được làm gì |
|---|---|---|
| Các shot file của một section (`src/scenes/<shot id>.ts`), các part file của nó (`src/scenes/parts/<section id>-*`), thư mục chụp của nó (`out/<section id>/`) | Builder của section đó | Ghi |
| Engine (`src/engine/`), bộ kit chung (`src/scenes/parts/kit-*.ts`), overlay (`src/scenes/overlay.ts`), placeholder card (`src/scenes/storyboard-card.ts`), studio (`src/main.ts`, `vite.config.ts`), công cụ chụp (`scripts/render.ts`) | Lead | Đọc |
| Các cast file của phim có nhân vật (tên `cast-<name>.ts` trong `src/scenes/parts/`, xem `characters-and-story.md`, mục 3) | Lead | Đọc. Hỏi lead khi thiếu một tư thế hoặc biểu cảm |
| Shot data và lời chữ (`shots.json`, `copy.json`) | Lead | Đọc. Ghi một trường được nêu tên, chỉ khi được cho phép |
| File được sinh ra: tài liệu storyboard (`STORYBOARD.md`), ranh giới shot (`data/film-sections.json`), thời điểm shot trong dữ liệu audio (`sections` của `data/audio.json`) | Bộ sinh (`scripts/build-shot-files.py`) | Không ai sửa tay |
| Treatment, authoring guide, quy tắc dự án | Lead | Đọc |
| File của builder khác | Builder đó | Đọc |
| Báo cáo | Mỗi builder tự viết báo cáo của mình | Đọc báo cáo section của mình từ các vòng trước |

Các quy tắc sở hữu:

1. Một builder sở hữu một section. Các shot trong một section dùng chung part, chung look và thường chung một thế giới, và các chỗ cắt bên trong là việc builder của nó phải khớp.
2. Builder cần thay đổi trong kit hoặc engine, hoặc phát hiện lỗi ở đó, thì nói trong báo cáo và tìm cách lách. Nó không chép code kit vào file của mình để sửa.
3. Builder nghĩ storyboard sai về section của mình thì nói trong báo cáo. Lead sửa shot data.
4. Builder dùng một part của section khác thì phụ thuộc vào builder của section đó. Nó báo cáo sự phụ thuộc, và lead quyết định part đó có chuyển vào kit chung không.
5. Khi kit chung thay đổi trong lúc các builder đang làm, lead báo cho mọi builder. Mỗi builder chụp lại những gì bị ảnh hưởng và báo kết quả. Một thư mục phim là bản sao của starter, nên một bản sửa lead làm trong engine hoặc kit của starter không tới được phim đã được sao trước đó: lead chép file đã sửa vào mọi phim đang làm, rồi báo cho builder của chúng. Từ thực tế: một guide nêu tên hai thiết lập post mà lead vừa thêm vào starter, trong khi engine riêng của phim, được sao trước đó, không có chúng.
6. Một thứ mà nhiều section cùng vẽ (một nhân vật, một vật mở ra được, một thiết bị) nằm trong kit cùng với các hook mà mọi section sẽ cần, không chỉ có đường viền: chỗ nó mở, chỗ gắn đồ, kích thước ở một chiều cao nhất định. Lead hỏi builder đầu tiên nó đã phải thêm gì, và chuyển phần đó vào kit trước khi các builder sau bắt đầu.
7. Quyền ghi shot data hiếm và hẹp. Nó nêu tên một shot và một trường, và chỉ được cấp khi builder tự mình tìm ra được giá trị đó, ví dụ vị trí và kích thước tại đó một phần tử trong shot của nó được trao cho một transition của engine.
8. Ai ghi một file dữ liệu chung thì đọc lại nó ngay trước khi ghi, chỉ đổi đúng trường mình định đổi, chạy bộ sinh, và kiểm tra các file được sinh ra. Một bản đọc từ đầu vòng có thể đã cũ.

Từ thực tế: một builder có tiêu đề trao một chữ cái lớn cho một transition của engine được cấp quyền đặt kích thước và điểm xoay của đúng transition đó trong shot data. Nó chạy bộ sinh và báo cả hai giá trị. Trong cùng những giờ đó lead sửa cùng file cho các section khác. Không ghi nhận mất mát nào. Quy tắc 8 là biện pháp phòng ngừa mất mát mà cách sắp xếp đó có thể gây ra. Các builder khác thấy một trường không còn khớp với shot của mình, để yên file và báo giá trị, rồi lead ghi nó vào.

## Authoring guide

Mỗi builder nhận một guide. Lead viết nó trước khi bất kỳ builder nào bắt đầu, cùng với treatment và bộ kit chung. Nó chứa những gì đúng cho mọi section, để brief có thể ngắn.

Starter không kèm guide. Lead viết một guide cho phim và giữ nó trong thư mục phim, cạnh `README.md`, với tên do lead chọn. Các mục 4, 5 và 9 của nó bắt đầu từ README của starter: "Adding a scene module" (khung của một module và các quy tắc cho cảnh), bản đồ file (các file kit trong `src/scenes/parts/`), và "Commands".

| STT | Mục của guide | Nội dung thuộc về mục đó |
|---|---|---|
| 1 | Bộ phim | Một đoạn: chủ đề, khán giả, điều người xem mang về, khung hình, frame rate, độ dài, nhạc. Hình thức bàn giao và hệ quả của nó cho một shot, ví dụ một mục tiêu frame time và không motion blur khi phim chạy real time |
| 2 | Cái gì cố định, cái gì là của bạn | Vài quy tắc cố định của phim, mỗi quy tắc kèm lý do. Các quyền tự do. Bảng nội dung "phải thể hiện, không bao giờ được thể hiện", cùng các ví dụ và đạo cụ đã có chủ. Các màu theo tên và cách dùng. Look mà mỗi section mượn |
| 3 | File của bạn | Bảng sở hữu, và phải làm gì khi cần thay đổi một file không thuộc builder |
| 4 | Một shot | Hợp đồng của một shot: khung của một module và các quy tắc không được phá |
| 5 | Bộ kit | Bảng các file kit và mỗi file cung cấp gì. Các bẫy đã biết của thư viện. Các tính năng trình duyệt của chủ phim thiếu. Cỡ chữ tối thiểu. Các glyph mà font thiếu |
| 6 | Camera | Tư thế là dữ liệu. Một chuyển động rời đi và lắng lại thế nào. Hình được "thở" theo cú kick đến mức nào. Khi nào khung khoá là lựa chọn đúng |
| 7 | Transition | Khoảng trống một shot để lại: điều gì xảy ra với các beat cuối và các beat đầu của nó. Các in-world transition builder tham gia, mỗi loại một dòng, và hình thay thế engine phát cho tới lúc đó |
| 8 | Lời chữ | Các cách một câu đến với người xem, ai đặt nó trong từng trường hợp, phép thử để bỏ lời chữ. Câu chữ đã duyệt và chính xác. Builder có thể đổi cách thể hiện và phải báo cáo |
| 9 | Lệnh | Type check, still, contact sheet, frame time. Các lần chụp xếp hàng sau một lock. Những gì bị cấm |
| 10 | Vòng lặp | Viết, chụp, nhìn, hỏi, sửa, đo. Rồi xem các shot liền nhau qua các chỗ cắt |
| 11 | Báo cáo của bạn | Viết ở đâu, các phần của nó, khối trạng thái |

Hợp đồng của một shot có bốn quy tắc không được phá.

| Quy tắc | Nghĩa |
|---|---|
| Một frame là một hàm của thời gian | Không đồng hồ thật, không số ngẫu nhiên không có seed, không trạng thái mang từ frame này sang frame kia. Một mô phỏng được chạy một lần lúc đầu vào một bảng rồi tra cứu |
| Thời gian được đếm bằng beat | Mọi sự kiện đọc dữ liệu beat của bản phân tích. Không gì được tính từ giây hay từ một con số tempo |
| Frame đầu tiên có sức nặng | Một shot bắt đầu trên một beat, thường là beat mạnh. Frame đầu của nó đã là một bức hình |
| Thứ nhảy bậc đọc theo frame, thứ chuyển động đọc theo sample | Một bộ đếm, một nhãn đổi, chữ nào đang hiện: thời điểm của frame. Một vị trí, camera, một đường đang được vẽ: thời điểm của sample |

Quy tắc cho chính guide:

1. Quy tắc cố định thì ít. Mọi thứ khác là của builder, và guide nói rõ như vậy.
2. Guide dặn builder đánh dấu một shot đọc ra như khái niệm khác, kể cả khi storyboard yêu cầu shot đó.
3. Guide là một file sống. Khi một báo cáo nêu tên một cái bẫy, lead thêm một dòng.
4. Đường dẫn trong guide là tương đối với thư mục phim, để guide vẫn dùng được khi chuyển sang máy khác.

Từ thực tế: ba dòng trong guide của phim thứ hai đến từ chính công việc. Thứ tự vẽ của vật thể trong suốt trong thư viện 3D và việc phải giải phóng một line batch đến từ báo cáo của builder. Lệnh cấm một tính năng canvas mà trình duyệt của chủ phim thiếu đến từ một lỗi chủ phim tìm ra.

## Brief cho một builder

Brief chứa những gì chỉ đúng cho section này. Thay mọi placeholder trong ngoặc nhọn.

```text
# Brief: section <section id>, <section name>

## Task
Build the <number> shots of section <section id>, bars <first bar> to <last bar>
of the music. When you finish, no placeholder card is left in these bars.
Idea of the section in one sentence: <what the viewer must understand>.
Look the section borrows: <look>. Key hue: <hue>.

## Read first, in this order
1. <path of the authoring guide, in the film folder>, the whole file
2. STORYBOARD.md: your section, and the shots on both sides of it
3. shots.json and copy.json, read only
4. <kit files in src/scenes/parts/ that matter most for this section>
5. <report of this section from an earlier round, if one exists>

## Files you may change
- src/scenes/<shot id>.ts, one for each of your shots; the file name is
  exactly the shot id
- src/scenes/parts/<section id>-*
- out/<section id>/ (pass --out to the capture tool)
Everything else is read only, the cast files (src/scenes/parts/cast-*.ts)
among them: ask the lead for a pose or an expression they lack.
<Only if leave is given:> You may change the field <field> of shot <shot id> in
shots.json. Read the file again immediately before you write. Change
nothing else in it. Run bun run shots. Report the old
and the new value.

## The music in your bars
| Bars | What the music does | What it carries |
|---|---|---|
| <bars> | <no drums, build, drop, break> | <problem, answer, what must be read> |

## The shots
| Shot id | Bars | Intent | Camera move | Comes in by |
|---|---|---|---|---|
| <shot id> | <bars> | <what the viewer must see, not how to draw it> | <move> | <transition> |

## Transitions
Leave room for:
- <shot id>: the last <n> beats lie under the transition lead of the next
  shot. What matters is over before that.
- <shot id>: the first <n> beats arrive under a transition tail. The first
  frame has weight, and no word to be read stands there.
Take part in:
- <kind> from <shot id> into <shot id>: <what is asked of the shot>.

## Words
| Sentence | Bars | How it reaches the viewer | Place | Reason |
|---|---|---|---|---|
| <kind> | <bars> | <plate, shot, none> | <top, middle, bottom> | <reason> |
The lower edge of a plate of <n> lines at the top is y <pixels>. The upper
edge of a plate at the bottom is y <pixels>.
The wording is approved. Use it exactly. You may wrap it again.

## Content boundaries
Must show: <one line>.
Must never show: <one line, taken from the neighbouring concepts>.
Examples and props that belong to other sections: <list>.
Test for every shot: could a viewer who cannot see the name call this shot by
the name of another concept? If yes, the shot is wrong. Say so in your report,
even when this brief asked for the shot.

## Practical rules
- Run commands from the film folder <path>. Use absolute paths.
- Captures run one at a time for the whole machine. The tool waits its turn.
- Do not start a browser, a server or a renderer. Do not stop a process that
  you did not start. Do not export video.
- The owner watches in <browser>. Do not use <features that browser lacks>.
- If the type check fails in a file that is not yours, say so and go on.
- <words that the shell of this machine refuses in a command, if any>

## Only for a rework
The shot as it is now shows: <list of its pictures>.
Must survive: <pictures the owner praised, pictures that carry the idea>.
May be dropped: <list, chosen by the lead>.
New job: <what changes and why>.

## Accepted when
- <criterion that can be checked on a capture>
- Frame time of every shot is measured and is at or under <target>.

## Report
Write to <reports folder>/<file name>. A later round is added to the same file
under a new heading. Parts:
- what each shot shows, in one or two sentences, and its files
- where you departed from the storyboard, and why
- what you decided for each sentence, and why
- frame time of each shot
- problems in the kit or the engine, and how you worked round them
- every figure or statement on screen that is not in <single source>
- proposals you did not build
- what you are not satisfied with
- unresolved questions

End your reply with:
Status: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT
Summary: one or two sentences
Concerns/Blockers: optional
```

Ghi chú về brief:

1. Cột "Intent" nói người xem phải thấy gì. Nó không nói vẽ thế nào.
2. Cho biết mép của các plate bằng pixel. Builder mà đoán độ sâu của plate sẽ bố cục shot nằm bên dưới nó.
3. Đừng chuyển cả cuộc hội thoại. Hãy đưa các quyết định mà section cần.
4. Khi builder trả lời `BLOCKED` hoặc `NEEDS_CONTEXT`, hãy đổi ngữ cảnh, phạm vi hoặc cách tiếp cận. Đừng gửi lại đúng brief cũ.

Từ thực tế: một builder giả định plate ở trên cùng sâu khoảng 250 pixel, rồi phát hiện với ba dòng nó xuống tới khoảng y 615. Ở một section khác, hai shot phải qua thêm một vòng bố cục, để không có chữ cần đọc nào nằm dưới một plate ba dòng.

## Vòng review

| Bước | Ai | Điều gì xảy ra |
|---|---|---|
| 1 | Builder | Dựng, chụp, nhìn, sửa, đo. Chạy motion check của `quality-gates.md` trên các chuyển động nhanh và ở các ranh giới timing của mình. Viết báo cáo và khối trạng thái |
| 2 | Lead | Đọc báo cáo trước: các điểm lệch, các đề xuất, danh sách "chưa hài lòng" |
| 3 | Lead | Mở contact sheet của builder. Tự chụp ở chỗ ảnh của builder không phủ tới một khoảnh khắc, một chỗ cắt với shot bên cạnh đã nạp, hoặc một nhận xét của chủ phim |
| 4 | Lead | Xem từng ảnh, và đánh giá nó theo bảng nội dung, look của shot tốt nhất trong section, kiểm tra đọc, kiểm tra sync và frame time |
| 5 | Lead | Gửi các điểm lại cho đúng builder đó, kèm lý do, hoặc chấp nhận bằng lời rõ ràng |
| 6 | Builder | Làm vòng đó và thêm vào báo cáo dưới một heading mới |
| 7 | Lead | Chụp lại và xem lại. Một điểm được đóng bằng một ảnh chụp, không bao giờ chỉ bằng lời của builder |

Công việc trả lại cho đúng builder đó vì nó giữ ngữ cảnh của section. Builder không sống lâu hơn session: báo cáo của nó là điểm xuất phát cho builder sau.

| Phần của một tin nhắn review | Nó chứa gì |
|---|---|
| Đã thấy gì, và lúc nào | Shot id, thời điểm tính bằng giây hoặc beat, và những gì có trong frame lúc đó |
| Sai ở đâu | Lý do, đối chiếu với một quy tắc của guide, bảng nội dung hoặc shot tốt nhất của section |
| Cần làm gì | Kết quả mong muốn. Phương tiện vẫn để builder lo |
| Cái gì được giữ | Các phần đang ổn, nêu tên, để vòng này để yên chúng |
| Quyết định về đề xuất của builder | Từng điểm lệch được duyệt hay không. Từng đề xuất được nhận hay bị từ chối, kèm lý do. Từng lần vượt frame time có được chấp nhận hay không |
| Lead tự đổi những gì | Các thay đổi trong kit, engine hoặc shot data mà builder phải chụp lại |

Giữ danh sách đủ ngắn để làm xong trong một vòng, và giữ mỗi vòng một loại câu hỏi (xem thứ tự các vòng bên dưới).

Từ thực tế: một tin nhắn review chứa ba đến năm điểm cho một section. Review của section mẫu có ba điểm: shot cuối yếu nhất, vật đại diện cho khái niệm quá nhỏ ở hai shot, và nhân vật bị cứng. Một tin nhắn review cho section khác chốt bốn việc, mỗi việc một dòng: duyệt một thay đổi các bước, duyệt một thay đổi timing, từ chối một in-world transition được đề xuất, chấp nhận các lần vượt frame time nhỏ. Một đề xuất thêm một in-world transition nữa bị từ chối kèm lý do: chỗ cắt đó nằm trong đoạn tĩnh, và các transition như vậy vốn nên ít.

## Thứ tự các vòng

| Vòng | Câu hỏi | Các điểm thuộc về nó |
|---|---|---|
| 1. Nội dung | Mỗi shot có thể hiện ý của chính nó, chứ không phải ý bên cạnh? Mọi ví dụ có đúng không? | Một shot đọc ra như khái niệm khác. Một ví dụ hoặc đạo cụ thuộc về section khác. Một dấu đánh lên thứ không hề sai |
| 2. Bố cục và tay nghề | Bức hình có được dựng tốt không? | Chủ thể quá nhỏ. Một phần frame trống. Thứ cần đọc nằm dưới plate. Frame đầu trống. Một sự kiện lỡ beat. Một shot làm bằng primitive trơn cạnh các shot được vẽ kỹ |
| 3. Hoàn thiện | Còn những việc nhỏ nào? | Nhãn chạm nhau, đánh số, một highlight, một bóng đổ |

Nội dung đi trước vì một shot đổi nội dung sẽ mất phần tay nghề đã bỏ vào nó. Một lần review xem hình đẹp tới đâu không tìm ra lỗi nội dung: hình vẫn đẹp.

Từ thực tế: ở một section, vòng hoàn thiện đi trước. Vòng nội dung sau đó viết lại hai shot, và một part file vừa được hoàn thiện bị xoá. Một vòng thứ ba sau đó lại bố cục lại hai shot mới.

Làm lại một shot mà chủ phim đã xem:

1. Xem shot như hiện tại, và ghi lại những gì xảy ra trong đó.
2. Đánh dấu những gì phải giữ lại: điều chủ phim đã khen, và điều mang ý tưởng.
3. Khi shot bị rút ngắn, chọn cái bị bỏ. Lựa chọn đó là của lead.
4. Đưa cả hai danh sách vào brief. Nói cho chủ phim biết cái gì bị bỏ.

Từ thực tế: một shot được dời tới cú drop đầu tiên và được giao mang tên của section. Brief mô tả nhiệm vụ mới và không nói gì về ba nhát cắt xuyên một tờ giấy mà shot đã thể hiện. Builder thay chúng đi. Chủ phim thấy ngay lần xem đầu: "Trước khi bạn sửa, shot cắt một tờ giấy thành ba tấm thẻ. Giờ cái đó mất rồi, mà nó hay." Việc đó tốn thêm hai vòng.

## Tải của máy

| Quy tắc | Được đảm bảo thế nào |
|---|---|
| Mỗi lúc chỉ một lần chụp cho cả máy | Một lock bên trong công cụ chụp. Lần chạy thứ hai chờ lần đầu, bất kể ai khởi động |
| Builder không mở trình duyệt, server hay renderer | Guide và brief nói vậy. Công cụ chụp tự mở server riêng và dừng nó khi xong |
| Không để server, trình duyệt hay watcher nào chạy sót | Lead theo dõi mọi tiến trình nó khởi động: lệnh, process id, port. Nó dừng một tiến trình theo đúng id sau khi xác nhận đó là gì, và kiểm tra lại sau đó |
| Không ai dừng tiến trình không phải của mình | Guide và brief nói vậy |
| Không xuất video trừ khi chủ phim yêu cầu trong cuộc hội thoại này | Công cụ chụp từ chối chế độ video. Sự cho phép một lần không được mang sang lần sau |
| Studio không làm nặng máy khi chủ phim không xem | Studio không vẽ gì khi đang tạm dừng |
| Một job nặng phải được báo trước | Lead nói nó sẽ chạy bao lâu và cách dừng, trước khi bắt đầu |

Cách lock hoạt động, như đã dựng trong thực tế:

| Thuộc tính | Hành vi |
|---|---|
| Hình thức | Một thư mục, `.render.lock`, chứa process id của chủ nó. Tạo thư mục hoặc thành công hoặc thất bại, nên hai lần chạy không thể cùng giữ nó. Công cụ của starter đặt nó trong thư mục gần nhất phía trên phim có chứa `.git`, nếu không thì thư mục gần nhất chứa `CLAUDE.md` hoặc `AGENTS.md`, nếu không nữa thì thư mục tạm của hệ thống; `RENDER_LOCK_DIR` ghi đè điều này. Mọi phim dưới cùng một gốc dùng chung nó |
| Chờ | Lần chạy thấy lock thì chờ và thử lại mỗi nửa giây |
| Lock mà chủ đã mất | Nó được xoá sau lần xem thứ hai, để tính cả khoảnh khắc giữa lúc tạo thư mục và lúc ghi id |
| Giới hạn | Một lần chạy bỏ cuộc sau mười lăm phút chờ |
| Giải phóng | Khi thoát và khi bị ngắt, và chỉ bởi chủ của lock |
| Server | Công cụ mở một server riêng không có live reload, để một file được lưu trong lúc chụp không làm trang tải lại. Nó chỉ dùng studio khi `--url` chỉ tới đó, và chỉ khi marker của trang ghi tên phim này (`title` trong `src/project-config.ts`). Builder bỏ `--url` đi |

Từ thực tế: ở phim đầu chín builder chụp cùng lúc và máy bị quá tải. Chủ phim yêu cầu: "Chạy render chậm thôi, và đừng mở nhiều song song như vậy. Máy tôi không chịu nổi." Ở phim thứ hai quy tắc trở thành: "Đừng xuất video nữa, nó tốn CPU máy tôi quá. Chỉ làm HTML thôi, rồi dựng một trang nối các cảnh lại để tôi bấm play."

## Mở rộng quy mô

Những gì đã làm trong thực tế:

| Phim | Section và shot | Builder | Khởi động thế nào | Agent khác |
|---|---|---|---|---|
| Phim đầu | 12 section, mỗi section dựng thành một module dài 3 đến 8 bar | 9, mỗi builder một section. Lead tự dựng 3 section, trước khi có quy tắc lead không dựng | Tất cả cùng lúc | 4 researcher đọc tác phẩm tham chiếu, 1 nghiên cứu dịch vụ nhạc, 1 agent dựng engine |
| Phim thứ hai | 8 section mỗi section 4 đến 8 shot và một nhóm 3 (tiêu đề, tóm tắt, thẻ kết): 54 shot | 9, mỗi builder một section hoặc một nhóm | Một builder trước, cho section mẫu. Sau khi review và chủ phim xem, tám builder còn lại cùng lúc | Không |

### Một tác phẩm ngắn

Một tác phẩm thuộc làn ngắn (`short-pieces.md`) có một builder cho cả tác phẩm, chạy model Opus mới nhất, và không có story writer. Nó sở hữu mọi scene file và mọi part file của tác phẩm. Brief của nó là mẫu ở trên với một section: bảng beat thay cho các shot, khung hình và các format, loop hoặc click nếu được yêu cầu, chất liệu thật cùng ghi chép nguồn, và công thức nó theo. Ở làn này lead cũng không dựng; chỉ chủ phim mới có thể gỡ quy tắc đó cho một tác phẩm. Review bằng still: một still cho mỗi beat của bar dày đặc nhất, mỗi lần đổi trạng thái, đường nối của loop, các beat chính của mỗi format.

### Model nào làm gì

Quy tắc của chủ phim, đặt cho skill này: khi agent là Claude, các sub-agent suy nghĩ thấu storyboard và các sub-agent dựng shot chạy model Opus mới nhất. Lead giữ model của chính nó.

| Vai trò | Model | Cách làm |
|---|---|---|
| Lead | Model của session lead | Nó quyết định và review |
| Story writer | Opus mới nhất | Khởi động agent có nêu tên model, ví dụ `model: "opus"`. Đưa nó brief, các ranh giới và bản đồ nhạc; yêu cầu một bản nháp và lý do |
| Builder | Opus mới nhất | Như trên. Mỗi section một builder |
| Researcher | Model của session lead, hoặc một model nhỏ hơn | Nó đọc và báo cáo |
| Trên một trợ lý khác Claude | Model mạnh nhất mà trợ lý đó có cho công việc dài và cẩn thận | Ghi trong báo cáo đã dùng model nào |

| Quy tắc | Lý do |
|---|---|
| Nêu tên model khi khởi động agent | Agent khởi động không có model sẽ lấy model của session, không phải điều chủ phim yêu cầu |
| "Mới nhất" là tra cứu, không phải nhớ | Tên model thay đổi. Dùng alias mà công cụ cung cấp cho Opus mới nhất, và nói đó là model nào |
| Lead vẫn sở hữu storyboard | Story writer viết nháp. Lead đối chiếu bản nháp với các ranh giới, viết shot data, và đưa cho chủ phim |
| Nói rõ mỗi agent chạy model nào | Trong phần bàn giao, và bất cứ khi nào chủ phim hỏi |

Từ thực tế: ở phim thứ hai lead chạy Fable 5.1 và tự viết storyboard; chín builder chạy Opus, vì chủ phim muốn xem model đó làm được gì. Mọi lỗi nội dung chủ phim tìm ra sau đó đều đến từ storyboard của lead, không phải từ builder. Một bộ óc thứ hai cho storyboard, với bảng ranh giới trong tay, là phương án chủ phim đã chọn.

Hướng dẫn rút ra từ thực tế đó:

| Tình huống | Builder |
|---|---|
| Một clip dưới 30 giây với một shot | Một agent. Không kit chung, không shot data, không builder |
| Một phim ngắn ít shot | Một builder lần lượt làm các shot |
| Section mẫu chưa được chấp nhận | Một builder |
| Nhiều section không phụ thuộc nhau, và kit chung đã ổn định | Mỗi section một builder |
| Hai shot là cùng một thế giới | Cùng một builder |
| Một in-world transition vắt qua ranh giới hai section | Hai builder của hai section đó. Lead ghi trong cả hai brief mỗi bên trao gì, và kiểm tra chỗ cắt với cả hai shot đã nạp |

Thêm builder khi section mẫu đã được chấp nhận, kit đã ổn định và các section độc lập. Lock khiến các lần chụp xếp hàng, nên nhiều builder hơn nghĩa là mỗi lần chụp chờ lâu hơn chứ không phải nhiều trình duyệt hơn cùng lúc.

Từ thực tế: chủ phim xem section mẫu khi nó đang được dựng, thấy nó "đẹp và đúng hướng", và nói có thể thêm builder cho các shot không phụ thuộc nhau.

## Builder báo cáo gì

| Phần của báo cáo | Lead làm gì với nó |
|---|---|
| Mỗi shot thể hiện gì, và file của nó | Đối chiếu với storyboard và bảng nội dung trước khi mở ảnh chụp |
| Các điểm lệch khỏi storyboard, kèm lý do | Duyệt hoặc từ chối từng điểm trong tin nhắn review. Ghi các điểm được duyệt vào shot data |
| Đã quyết định gì cho mỗi câu chữ | Cập nhật shot data, để overlay ngừng vẽ plate mà giờ shot tự mang |
| Frame time của mỗi shot | Chấp nhận phần vượt hoặc gửi trả lại |
| Vấn đề trong kit hoặc engine, và cách lách | Tự sửa kit, báo cho mọi builder, thêm một dòng vào guide |
| Con số và phát biểu trên màn hình không có trong nguồn duy nhất | Nhờ chủ phim hoặc người am hiểu lĩnh vực kiểm tra |
| Các đề xuất chưa được dựng | Quyết định khi nhìn cả bộ phim |
| Chưa hài lòng | Xem bên dưới |
| Câu hỏi chưa giải quyết | Trả lời từng câu. Câu hỏi về shot bên cạnh được trả lời từ báo cáo của bên cạnh |
| Khối trạng thái | `DONE` và `DONE_WITH_CONCERNS` đi tới review. `BLOCKED` và `NEEDS_CONTEXT` nhận một brief đã được đổi |

Cách lead dùng danh sách "chưa hài lòng":

1. Đọc nó trước khi xem ảnh chụp. Đó là bản tự review của builder.
2. Kiểm tra từng mục trên ảnh chụp. Danh sách chỉ chỗ cần nhìn. Nó không thay cho việc nhìn.
3. Phân loại từng mục: sửa ngay, chấp nhận và ghi lại, hoặc là chuyện của kit.
4. Tìm các mục lặp lại ở nhiều báo cáo. Chúng chỉ vào kit, công cụ hoặc guide, chứ không phải vào một builder.
5. Chuyển những gì còn mở vào các mục mở của phần bàn giao.

Từ thực tế: cả ba điểm lead gửi trả về section mẫu đều đã được builder nêu trong danh sách của chính nó. Bốn builder liệt kê phần dưới của frame bị trống, và các điểm của lead yêu cầu dùng hết cả frame. Builder của nhiều section báo cùng một bẫy của công cụ chụp: một still yêu cầu tại một beat rơi vào giữa hai frame và hiện một giá trị nhảy bậc hai lần. Lead sửa công cụ, giờ nó dời still về frame gần nhất. Một mục vẫn mở tới lúc bàn giao: một model và một bản vẽ của cùng một vật khác nhau ở một chi tiết.

## Các kiểu thất bại của điều phối

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Chủ phim phải hô dừng | Lead coi việc duyệt bảng nội dung là lệnh bắt đầu dựng, rồi làm tiếp sang palette, font và kit | Dừng ở cổng. Cho xem storyboard và animatic, và chờ một lệnh rõ ràng. Công việc không mã hoá nội dung lẫn look thì có thể tiếp tục |
| Lead đang viết code shot | Lead muốn có một mẫu, hoặc muốn đi nhanh hơn | Dừng lại. Giao thứ đã có cho builder của section đó kèm điểm yếu đã nêu tên. Viết brief và review |
| Chủ phim xin thêm một thứ, và mọi thứ bị đổi thành thứ đó | Lead hiểu một bổ sung thành một sự thay thế | Hỏi: thêm, hay thay? Nhắc lại yêu cầu bằng lời của mình trước khi đổi shot data |
| Một hình chủ phim thích đã mất sau một lần làm lại | Brief mô tả nhiệm vụ mới của shot mà không nêu shot đã thể hiện gì | Liệt kê các hình của shot trước khi viết brief. Đánh dấu cái phải giữ. Tự chọn cái bị bỏ, và báo cho chủ phim |
| Một hình đã mất không tra lại được | Repository không có version control, nên builder dựng lại hình từ ngữ cảnh của mình | Đưa repository vào version control trước vòng làm lại đầu tiên |
| Type check của builder lỗi ở một file không phải của nó | Một builder khác đang làm dở một thay đổi: một file import một part chưa viết hoặc vừa bị xoá | Builder nêu tên file trong báo cáo và làm tiếp. Nó không đụng vào file đó. Lead chạy type check cho cả app khi mọi builder đã báo cáo |
| Một lần chụp ghi lỗi từ một shot không nằm trong review, và lần chạy thứ hai thì sạch | Một builder khác lưu file trong lúc chụp | Chỉ nạp các shot đang review. Chụp lại trước khi coi lỗi đó là thật |
| Một thay đổi shot data bị mất, hoặc file được sinh không khớp dữ liệu | Hai người cùng ghi một file dữ liệu: lead, và một builder được cấp quyền | Giữ một chủ. Chỉ cấp quyền cho một trường được nêu tên. Mọi người ghi đều đọc lại file ngay trước khi ghi và chạy bộ sinh |
| Builder dựng một lỗi một cách trung thành và tốt | Lỗi nằm trong storyboard hoặc phác thảo của lead | Chạy kiểm tra nội dung ở giai đoạn storyboard. Dặn builder trong guide đánh dấu shot đọc ra như khái niệm khác |
| Nhiều builder mất một vòng vì cùng một bẫy | Mỗi bên tự gặp nó, và không gì truyền nó sang những bên khác | Khi một báo cáo nêu tên một bẫy, sửa công cụ hoặc thêm một dòng vào guide, và báo cho các builder còn đang làm |
| Máy quá tải, và chủ phim hỏi có tiến trình nào bị bỏ mồ côi không | Mỗi builder tự mở trình duyệt riêng để chụp | Một lock bên trong công cụ chụp. Builder không khởi động gì |
| Chủ phim hỏi vì sao có thứ đang render | Lead chạy một job nặng mà không hỏi | Hỏi trước. Nói job chạy bao lâu và cách dừng |
| Đã sửa mà lỗi quay lại y nguyên | Chẩn đoán là phỏng đoán | Tìm bằng chứng trước: mỗi tiến trình đang làm gì, trình duyệt báo gì |
| Một session sau không làm tiếp được một section | Các builder của session trước không còn tồn tại | Một builder mới bắt đầu từ guide, storyboard và báo cáo của section. Vì vậy hãy giữ mọi báo cáo đầy đủ |
| Builder trả lời `BLOCKED` lần thứ hai | Đúng brief cũ được gửi lại | Đổi ngữ cảnh, phạm vi hoặc cách tiếp cận |
