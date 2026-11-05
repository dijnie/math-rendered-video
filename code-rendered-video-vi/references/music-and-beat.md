# Nhạc và beat

File này bao quát phần nhạc của một phim code-rendered: nhạc đến từ đâu, chủ sở hữu chọn nó ra sao, beat, bar và các phần của nó được đo và kiểm tra thế nào, và hình dạng của nó quyết định hình dạng của phim ra sao. File cũng liệt kê các helper clock (đồng hồ) mà một shot dùng, để mọi sự kiện trên màn hình nằm trên một beat được đọc từ dữ liệu.

Nạp file này khi: phim có nhạc mà chưa có file audio cuối cùng; cần dựng, kiểm tra hoặc sửa một beat grid (lưới beat); storyboard cần độ dài của các section và shot tính bằng bar; một builder hỏi cách đặt một sự kiện lên beat; hoặc hình bị trôi lệch khỏi tiếng. Với nhạc soạn bằng code, hiệu ứng âm thanh và voice-over (lời dẫn), nạp thêm `sound-and-voice.md`.

## Quy tắc tóm tắt

| Quy tắc | Lý do |
|---|---|
| Không bao giờ bắt đầu một lần generate tốn phí mà không hỏi chủ sở hữu trước. Một lần đồng ý áp dụng cho một yêu cầu, không phải yêu cầu kế tiếp. | Tiền là của chủ sở hữu. |
| Quyền sử dụng thương mại là câu hỏi dành cho chủ sở hữu. Lead báo cáo những gì đã biết và những gì chưa biết. | Lead không thể xác minh một giấy phép. |
| Gu thẩm mỹ được đánh giá bằng tai của chủ sở hữu. Phép đo chỉ dùng cho timing. | Một bản nhạc đo tốt hơn không phải là bản nhạc chủ sở hữu thích hơn. |
| Một grid phải được xem trước khi được tin. | Một tracker có thể sai một beat mà vẫn in ra một tempo nghe hợp lý. |
| Sự kiện được đặt theo beat đọc từ dữ liệu, không bao giờ theo giây và không bao giờ từ một con số tempo. | Các bản nhạc không giữ một tempo duy nhất. |

## 1. Nhạc đến từ đâu

| Nguồn | Cần gì | Rủi ro gì |
|---|---|---|
| Một bản nhạc chủ sở hữu mang đến | File ở chất lượng đầy đủ, và lời xác nhận của chủ sở hữu về ai nắm quyền. | Độ dài và các phần của nó cố định. Phim theo chúng, hoặc bản nhạc được cắt theo bar (mục 7). |
| Một bản nhạc từ thư viện có giấy phép | Một giấy phép phù hợp với nơi phim sẽ được chiếu. | Giấy phép có thể không bao gồm nơi đó. |
| Một bản nhạc do dịch vụ generate tạo | Sự đồng ý của chủ sở hữu trước mỗi yêu cầu tốn phí, và một yêu cầu viết ra (mục 2). | Tempo có thể trôi, độ dài có thể khác yêu cầu, và quyền phải được kiểm tra. |
| Một bản score (tổng phổ) soạn bằng code | Một score viết dưới dạng dữ liệu và render bằng `bun run score` (`sound-and-voice.md`). Không phải mua gì, không phải tải gì. | Nó nghe sạch và tổng hợp, hoặc như một bản phác sạch của một họ nhạc cụ acoustic, không giống một ban nhạc. Chưa ai nghe thử các nhạc cụ của starter. |
| Một tracker module chủ sở hữu mang đến (MOD, S3M, XM, IT) | Một player render nó ra WAV, tức là phải cài đặt (ví dụ player dòng lệnh của libopenmpt); hoặc một parser đọc các pattern của nó, thứ chưa được dựng. | Timing của nó chính xác trong dữ liệu, nhưng chỉ dữ liệu mới nói được điều đó: xem bên dưới. |
| Không có nhạc: một voice-over, hoặc im lặng | Với giọng nói, thời điểm của từng từ (mục 10). Với im lặng, một độ dài tính bằng giây. | Không có beat grid đo được. Vẫn cần một grid để cắt: tạo một cái (`bun run make-grid`) hoặc soạn một bed (nền nhạc) nhẹ, và đặt giọng nói lên đó (mục 10). |

Một score soạn bằng code không cần phân tích: grid của nó được viết cùng với nó, chính xác, và các mục 4 đến 6 của file này không áp dụng cho nó. Mục 7 và 8 thì có. Hiệu ứng âm thanh, giọng nói hoặc một bed đặt lên một bản nhạc chủ sở hữu mang đến thì theo grid đo được của bản nhạc đó (`sound-and-voice.md`, mục 5.2).

### Nhạc tracker

Một tracker module (nhạc của các bản demo và game thập niên 1990: MOD, S3M, XM, IT) không phải là một bản thu âm mà là một score: các pattern gồm nhiều hàng, mỗi hàng là một bước mà ở đó mọi channel có thể bắt đầu một nốt, và một timing được ghi trong file. Một hàng kéo dài `2.5 / tempo × speed` giây, trong đó tempo và speed là các thiết lập riêng của module (tempo 125 và speed 6 cho 0.12 giây một hàng), và các effect bên trong pattern có thể đổi cả hai ở bất kỳ hàng nào. Vì vậy grid của một module được biết chính xác, không đều ở chỗ các effect đổi speed, và mọi nốt của mọi channel là một onset có thể ghi thẳng vào `onsets`, không cần đo gì cả.

Những gì cần để phát nó:

| Cách | Cho ra gì | Trạng thái |
|---|---|---|
| Render ra WAV bằng một module player (player dòng lệnh của libopenmpt, hoặc cái khác) | Một bản nhạc như mọi bản khác; rồi đo nó (mục 4), hoặc đọc grid của nó từ module | Phải cài đặt: cần chủ sở hữu đồng ý. Chưa thử |
| Đọc các pattern của nó bằng code, như dữ liệu | Grid chính xác và mọi nốt dưới dạng onset, và thứ tự các pattern làm music map | Chưa dựng. MOD là định dạng đơn giản; S3M và các định dạng khác tốn công hơn. Vẫn cần các sample bên trong module để nghe được |
| Phát trực tiếp trong trang bằng một player JavaScript hoặc WebAssembly | Âm thanh trong trình duyệt | Một package: chưa thêm. Clock của nó không phải clock của studio |

Cho đến khi chọn một trong các cách này cùng chủ sở hữu, hãy đối xử với một module như một bản nhạc: render nó một lần, có sự đồng ý của chủ sở hữu, và đo nó. Quyền của một module là câu hỏi của chủ sở hữu, như với mọi bản nhạc; nhiều module của cộng đồng demo scene mang điều khoản riêng của tác giả.

Hỏi chủ sở hữu dùng nguồn nào. Đừng chọn một dịch vụ generate chỉ vì máy có sẵn key cho nó. Các công cụ đã cài là lựa chọn, không phải yêu cầu bắt buộc.

Hai quy tắc áp dụng cho mọi nguồn. Không bao giờ bắt đầu một lần generate tốn phí mà không hỏi chủ sở hữu trước, và một lần đồng ý không bao gồm yêu cầu kế tiếp. Quyền sử dụng thương mại là câu hỏi dành cho chủ sở hữu: lead ghi lại những gì đã biết và chưa biết, và không tự quyết định.

Từ thực tế: cả hai phim tham chiếu đều dùng bản nhạc do Suno generate qua key4u. Một yêu cầu trả về hai clip. Độ dài yêu cầu bị bỏ qua: yêu cầu 145 giây và nhận về khoảng 207 giây. Link tới kết quả là tạm thời, nên các file được tải về ngay. Hóa đơn hiện ra muộn, khoảng 1.20 USD cho một yêu cầu và việc chuyển đổi hai clip của nó. Quyền sử dụng thương mại của các bản nhạc này chưa bao giờ được xác minh, và điều này được ghi nhận là còn bỏ ngỏ.

## 2. Viết yêu cầu cho nhạc generate

| Cần chỉ định gì | Thế nào | Các từ dùng trong yêu cầu thật |
|---|---|---|
| Thể loại | Hai tên thể loại, rồi các nhạc cụ mang nó. | "electro house, bass house", "punchy four-on-the-floor kick", "growling syncopated bassline" |
| Tempo | Một con số bên trong đoạn mô tả style. | "130 bpm" |
| Không lời | Công tắc instrumental của dịch vụ, từ đó trong đoạn mô tả style, và một danh sách những thứ cần loại bỏ. | "instrumental"; loại bỏ: "vocals, singing, rap, choir, spoken word, vocal chops" |
| Cấu trúc | Nhãn các phần theo thứ tự, mỗi nhãn một dòng, làm nội dung yêu cầu. | `[Intro]`, `[Build]`, `[Drop]`, `[Drop 2]`, `[Breakdown]`, `[Build]`, `[Final Drop]`, `[Outro]` |
| Build và drop | Các từ đòi hỏi tương phản giữa các phần. | "big build-ups, hard drops", "tense risers" |
| Một tiếng kick đều | Yêu cầu nó bằng tên. Beat tracker bám theo trống kick. | "four-on-the-floor kick", "clear eight-bar phrases" |
| Độ dài | Một số giây. Đừng trông cậy vào nó. | 145, 180 |

Những gì các dịch vụ hay bỏ qua:

| Yêu cầu | Nhận được |
|---|---|
| Độ dài 145 giây | Hai clip khoảng 207 giây |
| Độ dài 180 giây | Các clip 213, 233, 162 và 172 giây |
| 140 BPM | Một bản nhạc trôi từ khoảng 138.2 đến 139.6 BPM |
| Một phiên bản model có tên | Phản hồi không nói model nào đã chạy, nên không thể xác nhận |

Yêu cầu nhiều hơn một ứng viên. Các yêu cầu theo hai hoặc ba hướng khác nhau, sau đó chọn, đi tới một bản nhạc tốt nhanh hơn một yêu cầu cố mô tả đúng bản nhạc ngay lần đầu. Nêu số lượng yêu cầu và chi phí dự kiến khi xin chủ sở hữu đồng ý.

## 3. Chọn bản nhạc

| Bước | Lead làm gì |
|---|---|
| 1 | Đặt mọi ứng viên vào một thư mục dưới dạng file chất lượng đầy đủ. Không đưa bản nén để đánh giá. |
| 2 | Báo cho chủ sở hữu đường dẫn, cùng độ dài và tempo của từng ứng viên. |
| 3 | Chờ. Chủ sở hữu nghe và chọn. |
| 4 | Trả lời một nhận xét về cảm giác trong vài dòng, với tối đa một lựa chọn đơn giản: giữ bản này, hoặc yêu cầu một ứng viên mới theo một hướng được nêu tên. |
| 5 | Hỏi trước bất kỳ yêu cầu tốn phí mới nào. |
| 6 | Ghi lại lựa chọn: file nào, và đã qua xử lý hay chưa. |
| 7 | Dùng nguyên bản nhạc nếu nó vừa với độ dài phim cần. Mỗi chỗ nối là một rủi ro cho âm nhạc. |

Quy tắc: không dùng phép đo để tranh luận về gu. Phổ tần, mức bass, độ rộng stereo và số onset không giải thích được vì sao một bản nhạc có cảm giác đúng, và chúng không được chạy để đáp lại một nhận xét về cảm giác. Phép đo thuộc về timing, nơi nó đáng tin cậy.

Từ thực tế: chủ sở hữu nói một bản nhạc đã chọn thiếu chi tiết và bass không sâu. Lead đo phổ tần, tạo một bản đã xử lý, và gửi một yêu cầu tốn phí thứ tư tới Suno mà không hỏi. Chủ sở hữu dừng việc phân tích và giải quyết vấn đề trong một dòng: bản đã chọn ổn, còn các clip mới hơn chi tiết hơn nhưng rối. Những clip đo tốt hơn về mức bass và độ rộng stereo lại là những clip chủ sở hữu ít thích hơn. Phim giữ lựa chọn đầu tiên, không qua xử lý. Chủ sở hữu cũng có thể đã nghe bản nén mà studio phát, đó là lý do có bước 1.

## 4. Pipeline phân tích

Các script đi kèm starter (`assets/starter/analysis/`, bộ sinh trong `assets/starter/scripts/`). Đường dẫn trong chương này là tương đối so với một thư mục phim tạo từ starter. README của nó nói cách tạo môi trường Python trên từng hệ điều hành.

| Script | Đọc | Ghi |
|---|---|---|
| `analysis/analyze-beat-grid.py` | Bản nhạc | File phân tích mà engine nạp |
| `analysis/plot-beat-grid-qa.py` | Bản nhạc và file phân tích | `structure.png` và bốn ảnh `zoom-bar-NNN.png` |
| `analysis/track-beats-by-phase-lock.py` | Bản nhạc và file phân tích | Một file grid, dùng để sửa một lỗi đếm sai (mục 5) |
| `analysis/edit-track-by-bars.py` | Bản nhạc, file phân tích và một file edit | Một bản nhạc đã cắt và file grid của nó (mục 7) |
| `scripts/build-shot-files.py` | Shot list và grid | Ranh giới các shot tính bằng giây, bên trong file phân tích |

```sh
P=analysis/python-env/bin/python
$P analysis/analyze-beat-grid.py IN.wav OUT.json [--sections sections.json] [--bpm-min 125 --bpm-max 180] [--bar-offset N]
$P analysis/plot-beat-grid-qa.py IN.wav ANALYSIS.json OUT_DIR
```

Chạy mỗi lần một phân tích trên máy mà chủ sở hữu đang làm việc. Các thư viện được pin trong `analysis/requirements.txt`, như khi được resolve trên macOS; trên hệ điều hành khác, cài bộ không pin nếu một pin bị lỗi.

| Bước | `analysis/analyze-beat-grid.py` làm gì |
|---|---|
| Envelope (đường bao) | Nó lọc bản nhạc thành các dải tần và lấy amplitude envelope của mỗi dải từ analytic signal. Không dùng cửa sổ loudness ngắn trên dải trầm, vì nó bám theo dạng sóng và báo mọi chu kỳ là một attack. |
| Onset của kick | Nó làm mượt envelope dưới 150 Hz cho đến khi gợn sóng của bassline biến mất, và lấy mỗi đỉnh của độ dốc làm một kick. Các kick cách nhau ít nhất 0.18 giây. Mỗi thời điểm được lùi về tiếng click của kick, được tìm trong dải từ 2000 đến 16000 Hz. |
| Beat tracking | Chu kỳ ban đầu là khoảng cách trung vị giữa các kick trong khoảng tempo. Danh sách beat sau đó bám theo các kick từng cái một. Một kick trong phạm vi 0.12 beat so với vị trí dự đoán được coi là nằm trên beat. Chu kỳ bám theo tempo một cách chậm rãi. |
| Beat không có kick | Chúng được chia đều giữa các beat đo được ở hai bên. Sau một khoảng trống 8 beat trở lên, grid chỉ khóa lại trên một kick mở đầu một chuỗi đều đặn. |
| Downbeat và pha của bar | Mỗi kick quay lại sau 8 beat không có kick bỏ phiếu cho vị trí của nó trong bar là beat một. Nếu phiếu không rõ ràng, sự thay đổi năng lượng từ beat này sang beat khác quyết định. `--bar-offset` ghi đè cả hai. |
| Section | `--sections` nhận một danh sách `{name, bar, bars}`. Bar được đếm từ downbeat đầu tiên, bắt đầu từ không. Script chuyển chúng thành giây. |

Các feature được giữ cho mỗi frame, 100 giá trị mỗi giây, mỗi giá trị được scale từ 0 đến 1:

| Tên | Dải | Ý nghĩa |
|---|---|---|
| `rms` | Mọi thứ đến 16000 Hz | Độ lớn |
| `low` | Dưới 150 Hz | Kick và bass |
| `mid` | 150 đến 2000 Hz | Phần thân của bản nhạc |
| `high` | 4000 đến 16000 Hz | Hi-hat và không khí |

Onset là các danh sách `[time, strength]`, với strength từ 0 đến 1. `kick` được đo như mô tả ở trên. `snare` chứa các attack trong dải từ 180 đến 2500 Hz, và `hat` chứa các attack trong dải từ 7000 đến 16000 Hz. Hai cái này là các attack trong một dải, không phải nhạc cụ được nhận dạng. Hãy đọc chúng là "có thứ gì đó sắc xảy ra trong dải này".

Hình dạng của file phân tích (`data/audio.json` của một phim):

| Khóa | Kiểu | Nội dung |
|---|---|---|
| `source` | văn bản | Đường dẫn của bản nhạc được phân tích |
| `duration` | số | Độ dài tính bằng giây |
| `bpm` | số | Tempo trung vị. Chỉ để hiển thị, không bao giờ dùng cho timing |
| `fps` | số | Tốc độ của các envelope, 100 |
| `beats` | danh sách số | Thời điểm của mọi beat tính bằng giây. Các khoảng cách không đều |
| `downbeats` | danh sách số | Thời điểm của beat đầu tiên của mọi bar |
| `sections` | danh sách `{name, start, end}` | Một mục cho mỗi shot, tính bằng giây, dù khóa tên là sections |
| `features` | danh sách dưới `rms`, `low`, `mid`, `high` | Các envelope |
| `onsets` | danh sách dưới `kick`, `snare`, `hat` | Các cặp `[time, strength]` |
| `notes` | object | Bằng chứng để kiểm tra grid: `beats_measured`, `beats_interpolated`, `kicks_total`, `grid_source`, `kick_minus_beat_ms`, `click_lag_ms`, `local_bpm_every_16_beats`, `bar_offset`, `reentry_votes`, `novelty_by_offset`, `measured_flags`, `stems` |

Một file grid, do script phase-lock và script edit ghi ra, nhỏ hơn: `duration`, `beats`, `downbeats`, `joins`, `source`, và `notes` hoặc `edit`. Beat đầu tiên của nó là beat một của một bar. Nó không có envelope, nên script plot không đọc được. Truyền nó cho `analysis/analyze-beat-grid.py` với `--beats-from` để có một file phân tích đầy đủ.

## 5. Kiểm tra grid

| Kiểm tra | Thế nào | Đạt khi | Không thấy được gì |
|---|---|---|---|
| Bằng mắt | Chạy script plot và mở các ảnh. Mỗi ảnh zoom hiển thị hai bar của dải trầm với grid đè lên: đường đỏ là downbeat, đường xanh là beat. | Một kick bắt đầu trên mỗi đường, trong cả bốn ảnh. | Một lỗi đếm sai. Các beat vẫn nằm trên kick ở hai bên của nó. |
| Bằng đếm | So số beat với độ dài bản nhạc chia cho chu kỳ beat trung vị. Đọc `local_bpm_every_16_beats` và `reentry_votes`. | Số đếm khớp, tempo cục bộ không có bước nhảy, và các phiếu rơi vào một vị trí trong bar. | Một grid sớm hoặc trễ một vài mili giây cố định. |
| Bằng tai | Trộn một tiếng click trên mỗi beat lên bản nhạc và để chủ sở hữu nghe ở đầu, giữa và cuối. | Tiếng click và tiếng kick nghe như một. | Nó phụ thuộc vào người nghe. Đây là bước kiểm tra cuối cùng, không phải một phép đo. |

Không script nào trộn click lên bản nhạc. Môi trường phân tích có một hàm cho việc này (`librosa.clicks`), nhưng chưa có gì gọi nó. Studio của starter có một nguồn `click` trên công tắc nhạc, phát grid một mình; chuyển qua lại giữa nó và bản nhạc (`M`) tại cùng một thời điểm là một cách kiểm tra thô. Ngoài ra kiểm tra bằng tai được làm trong studio: một shot chưa dựng được hiển thị thành một card nhấp nháy theo mỗi beat, và chủ sở hữu xem nó so với tiếng kick.

| Lỗi | Dấu hiệu | Cách phát hiện | Cách sửa |
|---|---|---|---|
| Tempo trôi trong một bản nhạc generate | Hình đúng nhịp ở đầu và trễ dần về sau. | So khoảng cách giữa các kick ở đầu và ở cuối. Đọc `local_bpm_every_16_beats`. | Bám theo các kick. `analysis/analyze-beat-grid.py` làm việc này, và engine chấp nhận thời điểm beat không đều. Không bao giờ dựng lại thời điểm beat từ `bpm`. |
| Đếm sai trong một đoạn dài không có kick rõ: một breakdown, hoặc một drop nơi bass side-chain che mất kick | Tempo cục bộ nhảy trong một đoạn rồi trở lại. `reentry_votes` bị chia. Mọi thứ sau đoạn đó lệch một beat. | Đọc `measured_flags` để tìm một chuỗi dài các số `0`. Đếm số beat trong chuỗi đó so với độ dài của nó và chu kỳ beat ở hai bên. | Chạy `analysis/track-beats-by-phase-lock.py`. Nó bắt đầu từ chuỗi beat dài nhất mà phân tích kick đo được, và đi ra hai phía từng beat một. |
| Một pickup bar (bar lấy đà) | Trong `structure.png` mọi bậc năng lượng rơi lệch một bar về bên phải của một đường phrase. Mọi phrase của phim bắt đầu sớm một bar. | Tìm chỗ kick quay lại sau một đoạn không có nó. Chia số bar đó cho 8 và đọc phần dư. | Để nguyên grid. Đếm phrase từ bar 1, và viết các bar của shot list cho khớp. |

Script phase-lock dự đoán beat kế tiếp từ chu kỳ hiện tại. Nó tìm một kick trong phạm vi 32 mili giây quanh dự đoán, và nếu không có thì tìm bất kỳ onset sắc nào. Nó dịch beat bằng một nửa độ chênh lệch, và giữ chu kỳ trong phạm vi 2 phần trăm so với chu kỳ ban đầu. Nó bắt đầu từ một chuỗi beat đo được vẫn còn 16 beat sau khi bỏ hai beat ở mỗi đầu.

```sh
$P analysis/track-beats-by-phase-lock.py IN.wav KICK_ANALYSIS.json OUT_GRID.json [--bar-offset N]
$P analysis/analyze-beat-grid.py IN.wav OUT.json --beats-from OUT_GRID.json --sections sections.json
```

Sau lệnh thứ hai, đọc `kick_minus_beat_ms`. Đó là khoảng cách từ mỗi beat tới kick của nó trong audio, dưới dạng trung vị và phân vị thứ 95. Cùng lệnh đó kiểm tra một bản đã xử lý của một bản nhạc so với grid của bản gốc: việc xử lý không được dịch chuyển timing.

Cách đọc nơi các phrase bắt đầu từ `measured_flags`: chuỗi văn bản chứa một ký tự cho mỗi beat, `1` cho một beat có kick. Một số `1` sau tám số `0` trở lên là một kick quay lại. Chỉ số của nó chia cho 4 là bar của nó, nếu `bar_offset` là 0. Phrase dài 8 bar, nên phần dư của bar đó chia cho 8 là như nhau cho mọi điểm bắt đầu phrase thật. Hai câu hỏi riêng biệt không được trộn lẫn: beat nào là beat một của một bar (`bar_offset`), và bar nào là bar một của một phrase (pickup).

Từ thực tế: bản nhạc của phim đầu tiên trôi từ khoảng 138.2 đến 139.6 BPM, và một grid với một tempo cố định lệch tới 65 mili giây. Sáu vòng fit grid đã tốn công trước khi các khoảng cách thô giữa các kick cho thấy chính tempo đang dịch chuyển. Sau khi sửa, grid nằm trên các kick với khoảng cách trung vị 1.5 mili giây. Trên bản nhạc của phim thứ hai, kick tracker trả về 376 beat, tempo cục bộ 132.3 BPM ở bốn cửa sổ liên tiếp so với khoảng 130 ở chỗ khác, và các phiếu 1, 2, 0 và 1. Grid phase-lock trả về 375 beat, tempo cục bộ giữa 129.9 và 130.5 BPM, và các phiếu 5, 0, 0 và 0. Nó khóa trên một kick cho 238 beat, trên một onset khác cho 135, và không trên gì cho 2, và khoảng cách trung vị tới các kick là 0.0 mili giây. Trong bản nhạc đó kick quay lại ở bar 9, 41, 65 và 81. Cả bốn đều để lại phần dư 1, nên bar 0 là một pickup và các phrase bắt đầu ở bar 1, 9, 17 và tiếp tục. Một lần quay lại thứ năm ở bar 75 đến sau một quãng dừng chỉ hai bar: một break bên trong một phrase, không phải điểm bắt đầu phrase.

## 6. Music map (bản đồ nhạc)

Music map đặt tên các phần của bản nhạc tính bằng bar. Nó là một bảng trong storyboard, và được làm trước khi bất kỳ shot nào có độ dài.

| Phần | Là gì | Cách tìm |
|---|---|---|
| Intro | Phần mở đầu, trước kick đầu tiên | `measured_flags` bắt đầu bằng một chuỗi `0`. Dải trầm yếu trong `structure.png`. |
| Build | Những bar cuối trước một drop, nơi căng thẳng tăng | Các bar trước khi kick quay lại. Dải trầm vẫn yếu. |
| Drop | Kick quay lại trên beat một và bản nhạc ở trọng lượng đầy đủ | Một số `1` sau một chuỗi dài `0` trong `measured_flags`. Cả ba dải đều mạnh trong `structure.png`. |
| Break | Một quãng dừng ngắn của trống bên trong một phrase | Một chuỗi `0` kéo dài một hoặc hai bar. |
| Breakdown | Một đoạn dài không có kick, một phrase hoặc gần như vậy | Một chuỗi `0` kéo dài nhiều bar, ở giữa bản nhạc. |
| Outro | Đoạn kết, nơi bản nhạc mỏng dần | Các dải giảm xuống ở những bar cuối của `structure.png`. |

| Bước | Lead làm gì |
|---|---|
| 1 | Kiểm tra grid trước (mục 5). Một map trên grid sai thì sai ở mọi nơi. |
| 2 | Mở `structure.png` và đọc năng lượng của mỗi bar trong ba dải. |
| 3 | Đọc các chuỗi `0` và `1` trong `measured_flags` và chuyển điểm kết thúc của chúng thành số bar. |
| 4 | Đánh dấu các điểm bắt đầu phrase và xác nhận chúng cách nhau 8 bar. |
| 5 | Đặt tên mỗi phần và viết map: phần, bar đầu, số bar, có trống hay không. |
| 6 | Trình map cho chủ sở hữu cùng với storyboard. Lead không nghe được bản nhạc, nên chủ sở hữu xác nhận vị trí các drop. |

Bar trong map được đếm từ không, từ downbeat đầu tiên. Shot list và `--sections` đếm cùng cách.

## 7. Trao câu chuyện cho âm nhạc

| Phần của nhạc | Nội dung phù hợp | Lý do |
|---|---|---|
| Intro không trống, hoặc một build | Một vấn đề lớn dần | Căng thẳng trong âm thanh chở căng thẳng trong câu chuyện. |
| Drop | Một sự lộ diện: câu trả lời, hoặc tên của thứ đó | Khoảnh khắc nặng nhất của nhạc gặp khoảnh khắc quan trọng nhất của section. |
| Break, nơi trống ngừng | Chữ cần được đọc | Không gì tranh chấp với chữ. Camera có thể đứng yên. |
| Phrase drop | Nhịp cắt nhanh nhất của phim | Phrase chở một cú cắt ở gần như mỗi bar. |
| Breakdown | Chờ đợi, một góc nhìn lặng lẽ, một chuyển động chậm của camera | Bản thân âm nhạc đã lùi lại. |
| Outro | Phần recap và câu kết | Phim kết thúc cùng bản nhạc. |

Độ dài của phim theo các phrase như thế nào:

| Đơn vị | Quy tắc |
|---|---|
| Section | Bắt đầu nơi một phrase bắt đầu, và kéo dài một số nguyên bar. Các section có thể khác nhau về độ dài. |
| Shot | Bắt đầu trên một downbeat. Độ dài của nó được viết bằng bar trong shot list. |
| Transition vào một drop | Lấy các beat cuối của shot trước drop. Những gì quan trọng trong shot đó phải xong trước chúng. |
| Chữ | Nằm bên trong section của chính nó, và ở lại đủ lâu để đọc được. |

Sau mỗi thay đổi shot list, chạy `scripts/build-shot-files.py`. Nó dừng nếu hai shot để lại một khoảng trống hoặc chồng nhau, hoặc nếu một caption chạy ra ngoài section của nó. Sau đó nó ghi ranh giới các shot vào file phân tích tính bằng giây.

Khi câu chuyện và âm nhạc không khớp:

| Lựa chọn | Dùng khi | Chi phí |
|---|---|---|
| Đổi độ dài của câu chuyện | Bản nhạc vừa với độ dài phim cần. | Không tốn gì cho nhạc. Câu chuyện uốn theo. |
| Dời các section sang phần khác của bản nhạc | Thứ tự câu chuyện tự do. | Chỉ các section bị dời phải dựng lại. |
| Cắt và nối bản nhạc theo bar | Bản nhạc quá dài, hoặc một phần phải bỏ. | Mỗi chỗ nối là một rủi ro cho âm nhạc. |
| Yêu cầu một bản nhạc mới | Không cách nào ở trên hiệu quả. | Tốn phí. Hỏi chủ sở hữu trước. |

Cắt theo bar được làm bằng `analysis/edit-track-by-bars.py`. Mỗi chỗ nối nằm vài mili giây trước một downbeat, nên tiếng click của kick kế tiếp không bao giờ bị cắt. Grid được mang qua cú cắt và không bị phát hiện lại. File edit ghi tên các bar cần giữ:

```json
{"lead_ms": 15, "crossfade_ms": 10, "fade_in_ms": 400, "fade_out_s": 3.0,
 "segments": [{"src_bar": 3, "bars": 60}, {"src_bar": 117, "bars": null}]}
```

```sh
$P analysis/edit-track-by-bars.py IN.wav ANALYSIS.json EDIT.json OUT.wav OUT_GRID.json
$P analysis/analyze-beat-grid.py OUT.wav OUT.json --beats-from OUT_GRID.json --sections sections.json
```

Từ thực tế: phim đầu tiên cắt bản nhạc từ 207 xuống 134.9 giây thành bốn đoạn. Chất liệu chỉ bị bỏ đi và không có gì được sắp xếp lại theo thứ tự mới. Phim thứ hai dùng nguyên bản nhạc, 172.4 giây. Các section của nó kéo dài từ 8 đến 14 bar và các shot kéo dài 1, 2 hoặc 3 bar. Năm transition vào drop của nó nằm ở bar 9, 41, 65, 75 và 81, chính là các bar mà dữ liệu cho thấy kick quay lại. Mỗi cái lấy 2 beat từ shot trước. Khi chủ sở hữu dời một section lên đầu và một section khác xuống cuối, hai section đổi chỗ trong nhạc, và sáu section ở giữa giữ nguyên bar của chúng và không cần dựng lại.

## 8. Clock mà một shot dùng

Ba file của starter chứa clock. Chúng không đếm từ cùng một con số. Trong code, một shot được gọi là scene.

| File | Đếm gì | Đếm từ |
|---|---|---|
| `src/engine/audio.ts` | Beat và bar của cả bản nhạc | Không, tại beat đầu tiên |
| `src/engine/beat-cues.ts` | Bar và beat theo cách nhạc công đếm | Một |
| `src/scenes/parts/kit-frame.ts` | Số beat kể từ khi shot bắt đầu | Không, tại frame đầu tiên của shot |

| Helper | Trả về gì | Cách dùng điển hình |
|---|---|---|
| `audio.timeOfBeat(i)` | Thời điểm tính bằng giây của beat `i`. Cho phép phân số. | Thời điểm của một beat |
| `audio.beatAt(t)` | Chỉ số beat tại thời điểm `t`, kèm phần lẻ | Beat tại một thời điểm |
| `audio.barAt(t)` | Chỉ số bar tại thời điểm `t`, từ các downbeat | Bar tại một thời điểm |
| `audio.nearestBeat(t)` | Thời điểm của beat gần `t` nhất | Đưa một thời điểm lên grid |
| `audio.section(t)` | Mục của `sections` chứa `t` | Shot nào đang phát |
| `f.beat`, `f.bar`, `f.beatPhase`, `f.barPhase` | Chỉ số beat và bar của cả bản nhạc tại frame này, và phần lẻ của chúng | Một readout (hiển thị số), hoặc một nhịp đập không quan tâm shot bắt đầu ở đâu |
| `audio.env(name, t)`, `audio.envPeak(name, t)` | Một giá trị envelope từ 0 đến 1, hoặc đỉnh của nó trong những khoảnh khắc vừa qua | Một phản ứng nhỏ, liên tục với âm thanh |
| `audio.hit(kind, t)` | Một nhịp đập suy giảm sau mỗi onset của loại đó | Phản ứng với các cú đánh trống thật |
| `timeOfPosition(grid, pos)` | Thời điểm của một bar, beat và phần lẻ | Một cue viết là bar 3, beat 2 |
| `positionAt(grid, t)` | Bar, beat và phần lẻ tại thời điểm `t` | Một readout trong studio |
| `cueStateAt(grid, cue, t)` | `active`, `progress`, `tStart`, `tEnd`, `elapsed`, `remaining` | Chữ hiện từ vị trí này đến vị trí khác |
| `sceneClock(au, f)` | `beats`, `bars`, `bar`, `beat`, `phase`, `length` cho lần gọi này | Mọi thứ chuyển động |
| `frameClock(au, f)` | Như trên, tại thời điểm của frame đầu ra | Mọi thứ nhảy bậc: một bộ đếm, từ nào đang hiển thị |
| `sceneTime(au, f, beats)` | Thời điểm tính bằng giây của một beat của shot | Trao một beat cho code cần giây |
| `since(au, f, beats)` | Số giây kể từ một beat của shot, âm trước beat đó | Kể từ một beat: spring và nhịp đập |
| `hit(beats, at, halfLife)` | 0 trước `at`, rồi 1, giảm một nửa sau mỗi `halfLife` beat | Trên beat: một điểm nhấn |
| `over(beats, at, dur, fn)` | Một giá trị có ease từ 0 đến 1 trong `dur` beat | Một chuyển động bắt đầu trên một beat |
| `during(beats, at, until)` | True từ `at` cho đến `until` | Trong các beat: thứ gì đó hiển thị trong một khoảng |
| `steps(beats, at, every)` | Số bước nguyên kể từ `at` | Bộ đếm, và các cú cắt nhảy bậc theo beat |
| `groove(beats, every, offset, halfLife)` | Một điểm nhấn lặp lại | Một nhịp đập trên mỗi beat. Offset 0.5 là off-beat. Every 2 với offset 1 là backbeat. |

```ts
const k = sceneClock(audio, f);    // cho mọi thứ chuyển động
const kf = frameClock(audio, f);   // cho mọi thứ nhảy bậc
```

Hai dòng từ các shot thật của phim tham chiếu, một con dấu đóng xuống và một máy đánh bạc:

```ts
return { ...POST_LIGHT, zoom: 1 + 0.012 * hit(k.beats, STAMP, 0.25) };
return { ...POST_DARK, bloom: 0.6, vignette: 0.5, zoom: 1 + 0.008 * groove(k.beats, 1, 0, 0.2) };
```

Quy tắc: sự kiện được đặt theo beat đọc từ dữ liệu, không bao giờ theo giây và không bao giờ từ một con số tempo. Builder viết `at` là một beat của shot. Các helper chuyển nó thành thời gian qua grid đo được, nên một tempo trôi vẫn được bám theo từng beat. Chuyển động được lên lịch theo beat và không bị điều khiển bởi độ lớn âm thanh. Một nhịp đập theo beat chỉ là gia vị: hai dòng trên dịch zoom khoảng một phần trăm. Nó không phải chuyển động chính.

## 9. Tempo và thể loại làm điểm khởi đầu cho buổi phỏng vấn

Bảng này là hướng dẫn, không phải quy tắc. Nó chứa những gì đã thử trên hai phim tham chiếu và phản ứng của chủ sở hữu. Một chủ sở hữu khác có thể nghe khác.

| Tempo | Thể loại yêu cầu | Cảm giác yêu cầu | Chủ sở hữu nói gì |
|---|---|---|---|
| Dưới 120 BPM | Nu-disco funk | Vui tươi, sôi động | Quá nhẹ nhàng. Bị loại. |
| Khoảng 130 BPM | Electro house, bass house | Năng lượng, mạnh mẽ | Được chọn. Chủ sở hữu thích thể loại này. |
| 138 đến 140 BPM | Techno | Build căng thẳng, drop mạnh, tối, uy lực | Một bản yêu cầu ở 140 được duyệt. Các ứng viên yêu cầu ở 138 không được chọn. |

Dùng nó để mở đầu cuộc trò chuyện: hỏi một bản nhạc chủ sở hữu đã thích, hỏi nhẹ nhàng hay dồn dập, và hỏi một thể loại theo tên. Rồi đề xuất hai hoặc ba hướng. Với một phim giải thích một chủ đề trên một bed không lời, chủ sở hữu này đã yêu cầu một beat thường trên 130 BPM.

## 10. Voice-over và caption canh theo lời nói

| Vấn đề | Chỉ có nhạc | Có giọng nói |
|---|---|---|
| Thứ dẫn dắt timing | Beat grid | Thời điểm của từng từ |
| Vai trò của nhạc | Quyết định các cú cắt | Là một bed, và được duck (hạ âm lượng) dưới giọng nói |
| Dữ liệu cần | Beat, downbeat, onset | Thời điểm từ. Đây là dữ liệu tốn công nhất để có |
| Caption | Đặt trên bar và beat | Đặt trên các từ, theo các nhóm từ nhỏ |

Lộ trình engine xử lý giọng nói qua `sound-and-voice.md`: giọng nói được viết thành các cụm trong `data/voice.json`, được một bước voice đọc thành mỗi cụm một file kèm thời điểm từ, được `bun run score` đặt sao cho từ đầu tiên của mỗi cụm rơi trên một beat, và được mix với bed bị duck bên dưới. Grid vẫn tiếp tục quyết định các cú cắt. Các nhóm caption đi vào `data/lyrics.json`, và một grid do score tạo mang một envelope `vocal` và các onset `vocal`, nên `f.a.vocal` và `f.a.vonset` hoạt động.

Những gì có và chưa có:

| Phần | Trạng thái |
|---|---|
| Một giọng Windows cục bộ với thời điểm bắt đầu của từ (`bun run voice:sapi`) | Đã dựng và chạy trên Windows 11. Chỉ có giọng tiếng Anh trên một hệ thống tiếng Anh nguyên bản |
| Thời điểm từ ước lượng từ âm thanh khi giọng không cung cấp | Đã dựng. Lệch tới một phần tư giây trên ví dụ |
| Ducking có look-ahead, một limiter, một mục tiêu loudness | Đã dựng |
| Các nhóm caption từ thời điểm từ, do overlay vẽ ở chân khung hình | Đã dựng; đã kiểm tra bằng still trên Windows 11 |
| Một giọng do người thu âm, với thời điểm từ transcription hoặc forced alignment | Chưa dựng. Cần một công cụ mà chủ sở hữu phải cho phép cài đặt |
| Một giọng nói, hiệu ứng và một bed trên một bản nhạc đo được, bản nhạc được duck, bản mix ở một mục tiêu loudness | Đã dựng (`track` trong score, `sound-and-voice.md`, mục 5.2). Đã thử với file test, chưa với một bản nhạc thật |

Một bản nhạc đo được không có envelope giọng nói trừ khi phân tích đã tạo ra một cái: `notes.stems` cho biết điều đó, và một shot đọc `vocal` khi đó nhận được 0. Lộ trình HyperFrames tuyên bố nó có giọng nói với thời điểm từ, transcription và một carve (khoét) nhạc dưới giọng nói; chưa cái nào được chạy trên máy này. Nếu phim không có giọng nói, bỏ qua tất cả phần này.

## 11. Lộ trình này so với HyperFrames

Nguồn: mục 6.9 và 9 của `hyperframes-facts.md`, và `sound-and-voice.md` cho lộ trình này. "Được tuyên bố" nghĩa là được viết trong một file skill của HyperFrames hoặc được công cụ của nó in ra. Chưa lệnh audio nào của nó được chạy trên máy này, nên hành vi của chúng chưa rõ. "Chưa được nghe" nghĩa là code đã chạy và đầu ra đã được đo, nhưng chưa ai nghe nó.

| Vấn đề | Lộ trình này | HyperFrames | Đánh dấu |
|---|---|---|---|
| Thời điểm beat | Đo từ các kick, không đều, kiểm tra so với audio | Một lệnh `beats` ghi `beats/<audio>.json` | Lệnh được tuyên bố. Định dạng và phương pháp của file chưa rõ. |
| Tempo trôi | Bám theo từng beat | "HyperFrames does not provide automatic waveform sync or drift correction." Một trong các quy tắc của nó dùng một grid đều. | Được tuyên bố |
| Map của cả một bản nhạc | `structure.png`, `notes`, music map | Một workflow `music-to-video` với một `audiomap.json` | Có tên nhưng chưa cài. Nội dung chưa rõ. |
| Envelope | Bốn dải, 100 giá trị mỗi giây | Các dải được trích xuất trước khi render, với `--fps 30 --bands 16`. Không phân tích trong lúc phát. | Được tuyên bố |
| Cắt bản nhạc theo bar | `analysis/edit-track-by-bars.py`, có mang theo grid | Không tìm thấy gì | Chưa rõ |
| Thời điểm từ | Từ một giọng Windows cục bộ (SAPI), hoặc ước lượng từ âm thanh (`sound-and-voice.md`, mục 9 và 10). Không có transcription | Giọng nói và transcription với timestamp của từ | Lộ trình này: đã chạy trên Windows 11. HyperFrames: được tuyên bố |
| Nhạc dưới giọng nói | Ducking có look-ahead, theo từng bus, trong `bun run score`, trên một bed soạn sẵn hoặc trên một bản nhạc đo được | Một carve, "required whenever music plays under a voice", cường độ mặc định 0.8 | Lộ trình này: đã chạy, chưa được nghe. HyperFrames: được tuyên bố |
| Loudness | Integrated loudness được đo và đặt về một mục tiêu, một limiter look-ahead, trong `bun run score`, cho một score soạn sẵn hoặc một bản nhạc có hiệu ứng | Một lệnh khớp loudness của một clip với clip khác | Lộ trình này: đã chạy. HyperFrames: được tuyên bố |
| Nhạc viết bằng code | Một score dạng dữ liệu render ra WAV với grid chính xác của nó (`bun run score`) | Không tìm thấy gì | Lộ trình này: đã chạy, chưa được nghe |
| Hiệu ứng âm thanh | Hiệu ứng tổng hợp và preset, và các file WAV thu âm được đặt theo đỉnh đo được của chúng, trên các cue theo bar và beat của một grid soạn sẵn hoặc đo được | Hiệu ứng đóng gói sẵn | Lộ trình này: đã chạy, chưa được nghe. HyperFrames: được tuyên bố |
| Tracker module | Không đọc; render và đo (mục 1) | Không tìm thấy gì | Chưa rõ |
| Tìm nhạc | Lựa chọn của chủ sở hữu, từ bất kỳ nguồn nào | Một catalogue với generate làm phương án dự phòng. Bảng prompt của nó có tempo cơ sở từ 92 đến 115 BPM. | Được tuyên bố |

## 12. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Hình đúng nhịp ở đầu và trễ dần về sau. | Thời điểm beat được tính từ một con số tempo. | Đọc thời điểm beat từ `beats`. Dựng grid từ các kick. |
| Bộ phát hiện kick trả về hàng trăm kick không hề có. | Một cửa sổ loudness ngắn trên dải trầm bám theo dạng sóng. | Dùng envelope của analytic signal, làm mượt nó, và lấy các đỉnh của độ dốc. |
| Thang thời gian lệch 0.227 phần trăm và sai số tăng tới 0.4 giây sau 3 phút. | Envelope được lấy mẫu mỗi `44100 // 1000` sample, tức là 1002.27 Hz. | Lấy mẫu tại các thời điểm chính xác. |
| Tempo cục bộ nhảy trong một đoạn rồi trở lại. | Tracker đếm thừa hoặc thiếu một beat ở chỗ không có kick rõ. | Track bằng phase lock, rồi đếm lại. |
| Mọi section bắt đầu một bar trước khi nhạc thay đổi. | Bar đầu tiên là một pickup. | Đếm phrase từ bar 1. |
| Các ảnh zoom trông đúng mà phim vẫn lệch một beat sau breakdown. | Các ảnh chỉ hiển thị bốn vị trí, và beat nằm trên kick ở hai bên của một lỗi đếm sai. | Kiểm tra bằng đếm cũng như bằng mắt. |
| Script plot lỗi trên một file grid. | Một file grid không có envelope, không có `bpm` và không có `fps`. | Tạo một file phân tích đầy đủ với `--beats-from` trước. |
| Một cue rơi lệch một bar hoặc một beat so với chỗ được viết. | Vị trí trong `beat-cues.ts` đếm từ một. Shot list và clock của shot đếm từ không. | Kiểm tra con số đó dành cho file nào. Bar 29, beat 0 của bản nhạc là beat 116. |
| Một bộ đếm hiển thị hai giá trị cùng lúc. | Một giá trị nhảy bậc được đọc từ clock của sample, không phải của frame. | Đọc các giá trị nhảy bậc từ `frameClock`. |
| Một shot đọc `drums`, `bass` hoặc `vocal` mà không gì chuyển động. | Phân tích không có stem. `notes.stems` cho biết điều đó. | Dùng `low`, `mid`, `high`, hoặc các onset. |
| Grid bị lệch sau khi bản nhạc được master hoặc chuyển đổi. | Việc xử lý đã dịch chuyển timing. | Phân tích file mới với `--beats-from` và đọc `kick_minus_beat_ms`. |
| Chủ sở hữu loại bản nhạc đo tốt hơn. | Phép đo đã được dùng để tranh luận về gu. | Trao các file. Chủ sở hữu nghe và chọn. |
| Chủ sở hữu biết về một khoản phí sau khi nó đã phát sinh. | Một yêu cầu tốn phí được gửi mà không hỏi. | Hỏi trước mỗi yêu cầu, và nêu chi phí. |
| Bản nhạc dài hơn phim rất nhiều. | Dịch vụ bỏ qua độ dài yêu cầu. | Cắt theo bar, hoặc để câu chuyện dùng nguyên bản nhạc. |
| Nhạc đánh xuống mà hình không có gì xảy ra. | Drop bị xử lý như một cú cắt thường, hoặc shot mở ra trên một khung hình trống. | Cho drop một build, một breath và một impact. Cho frame đầu tiên sức nặng. |
| Có thể nghe thấy một chỗ nối trong bản nhạc. | Cú cắt rơi vào giữa một bar, hoặc trên tiếng click của một kick. | Cắt vài mili giây trước một downbeat và crossfade. |
