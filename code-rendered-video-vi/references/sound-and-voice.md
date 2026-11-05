# Âm thanh và giọng nói

Cách một bộ phim đi theo lối engine có được âm thanh viết bằng code: một bản score (bản nhạc), các sound effect (hiệu ứng âm thanh) gắn với các sự kiện của hình (tổng hợp bằng code, hoặc file thu sẵn được đặt theo đỉnh của nó), một voice-over (lời dẫn) có caption chạy theo từng chữ, và bản mix nối tất cả lại, trên grid (lưới phách) tự soạn của phim hoặc trên một track (bản nhạc) hoàn chỉnh có grid đã được đo. Score là dữ liệu, và một script render nó offline ra file WAV. Một score đứng riêng cũng ghi ra beat grid của nó, và grid đó chính xác vì score được xây trên nó. Sau đó studio, engine và công cụ capture coi file này như mọi track khác.

Đọc file này khi: chủ phim muốn nhạc soạn bằng code, sound effect trên các sự kiện của hình (làm bằng code, hoặc từ file chủ phim chỉ định), một giọng đọc kịch bản, caption định thời theo lời nói, nhạc được duck (hạ âm lượng) dưới giọng nói hay dưới effect, một bản mix đạt mức loudness mục tiêu; hoặc khi một yêu cầu nói "compose the soundtrack yourself", "synthesize the sound", "SFX on every hit", "place each sound by its measured peak", "loudnorm to -14 LUFS", "in the style of", "narration", "text to speech", "every note comes from a collision".

Các đường dẫn là tương đối so với một thư mục phim, tức một bản sao của `assets/starter/`. Chưa có gì trong chương này được dùng cho một bộ phim thật. Cái gì đã chạy, và trên hệ thống nào, được nói ở chỗ cần thiết và liệt kê trong mục 12.

## Tóm tắt quy tắc

| Quy tắc | Lý do |
|---|---|
| Score là dữ liệu (`data/score.json`), được render bằng một script. Không âm thanh nào được tạo trong trang lúc nó phát | File studio phát chính là file mà bản export sẽ mang theo, và một still (ảnh tĩnh) ở bất kỳ khoảnh khắc nào cũng có đúng một âm thanh bên dưới |
| Một score đứng riêng giữ một tempo, và bar 0 bắt đầu ở thời điểm 0. Một score đè lên track (`track`) dùng grid đo được của track | Khi đứng riêng, grid được biết chính xác và được ghi ra, không phải đo. Khi đè lên track, mọi cue (điểm âm thanh) đi theo beat thật của track ở những chỗ nó trôi nhịp |
| Mỗi âm thanh có một hit point (điểm chạm), và hit point rơi đúng vào thời điểm score đưa ra | Riser kết thúc đúng vào sự kiện của nó, whoosh lên đỉnh đúng vào đó, trống bắt đầu đúng vào đó, file thu sẵn rơi đúng vào đỉnh đo được của nó |
| Sự kiện của hình và âm thanh của chúng được viết bằng cùng một hệ số: bar và beat, shot và beat, hoặc, với một mô phỏng, cùng một hàm | Hình và tiếng không thể lệch nhau khi cả hai đọc cùng một nguồn |
| Render là tất định: noise có seed, không dùng đồng hồ | Hai lần chạy cho ra cùng các byte. Hãy kiểm tra (mục 8) |
| Sạch hơn dày. Ít bè, mỗi bè một dải tần riêng | Chủ của các phim tham chiếu thích track sạch hơn track rối |
| Gu được đánh giá bằng tai. Các con số loudness là để giao hàng, không phải để tranh luận về gu | `music-and-beat.md`, mục 3 |
| Bản quyền của một track hay một file sound effect là câu hỏi của chủ phim | Lead ghi lại nguồn và giấy phép như chủ phim đưa ra, và không tự quyết |
| "Theo phong cách" một tác phẩm có tên thì lấy phong cách của nó, không bao giờ lấy giai điệu | Mục 4.5 |
| Một giọng đọc rời khỏi máy, hoặc tốn tiền, cần chủ phim đồng ý, mỗi lần | Giọng cloud gửi văn bản tới một công ty. Giọng trả phí tốn tiền |
| Cài một voice engine, một aligner (công cụ căn chỉnh) hay một decoder cần chủ phim đồng ý | `environment.md` |

## 1. Khi nào nên soạn bằng code

| Tình huống | Soạn bằng code | Một track hoàn chỉnh (`music-and-beat.md`) |
|---|---|---|
| Yêu cầu đòi điều đó ("compose the soundtrack yourself, fully synthesized, no samples") | Có | |
| Một tác phẩm ngắn 10 đến 30 giây với cú hit trên mọi sự kiện | Có: mỗi cú hit được viết đúng chỗ hình cần | Có thể, nếu track có sẵn các cú hit |
| Sound effect trên các sự kiện của hình, đè lên một track chủ phim cung cấp hoặc đã mua | Các effect và bản mix: một score có `track` (mục 5.2) | Track, đo trước |
| Effect thu sẵn mà chủ phim chỉ định ("use my SFX folder", một thư viện miễn phí bản quyền) | Đặt theo đỉnh đo được của chúng (mục 5.1) | |
| Một voice-over với một lớp nền (bed) bên dưới | Lớp nền và bản mix | Lớp nền, nếu chủ phim mang tới |
| Một bài hát có phối khí phong phú, một thể loại chủ phim yêu thích, một nhạc cụ thật | | Có. Vài nhạc cụ tổng hợp không thay được nó |
| "Theo phong cách" một nhạc phim, một thể loại, một thời kỳ | Một bản phác phong cách (mục 4.5) | Khi chủ phim muốn đồ thật |
| Chủ phim muốn chọn giữa các ứng viên bằng tai | Hai hoặc ba score theo các hướng khác nhau làm ra rẻ | Tạo nhạc bằng dịch vụ thì trả phí; hãy hỏi |
| Một tác phẩm phát trực tiếp theo cú click, có tiếng ngay từ cú click đầu | Các âm thanh được render ở đây thành file WAV ngắn, trang phát chúng khi click | Tổng hợp trực tiếp trong trang (Web Audio) chưa được xây |

Một score viết bằng code không thể trôi tempo và không bao giờ cần sửa grid, vì grid là bộ xương của nó. Nó nghe đúng như bản chất của nó: sạch, tổng hợp, điện tử, hoặc một bản phác sạch của một họ nhạc cụ acoustic. Hãy nói điều đó với chủ phim trước khi chọn nó cho một bộ phim cần sự ấm áp hay một nhạc cụ thật.

## 2. Pipeline

| Bước | Lệnh | Đọc | Ghi |
|---|---|---|---|
| Giọng (chỉ khi có voice-over) | `bun run voice:sapi`, hoặc một bước giọng khác (mục 9) | `data/voice.json` | `audio/voice/<id>.wav`, `data/voice-words.json` |
| Score | `bun run score` (`scripts/make-score.ts`) | `data/score.json`, `shots.json`; khi có giọng thì `data/voice.json`, `data/voice-words.json` và các file phrase; khi có track thì track và `data/audio.json` đo được của nó; các file sample; các cue module | File WAV đặt tên bởi `out` (`audio/score.wav`); `data/audio.json` cho score đứng riêng; khi có giọng thì `data/lyrics.json` |
| Thời gian shot | `bun run shots` | `shots.json`, `copy.json`, `data/audio.json` | Thời gian shot trong `data/audio.json`, `STORYBOARD.md`, `data/film-sections.json` |
| Nghe | `bun run studio`, công tắc nhạc ở `score` | `audio/score.wav` | Không gì cả |

`bun run score -- --check` kiểm tra score và giọng rồi in ra những gì sẽ được tạo, mà không ghi gì. Mỗi lỗi được in thành một dòng đơn giản, và không gì được ghi. `--score <file>` render một file score khác; `--no-grid` chỉ ghi file WAV (mục 8).

Code nằm trong `src/sound/`. Không file nào trong đó import thứ gì của Node hay của trang.

| File | Chứa |
|---|---|
| `src/sound/dsp.ts` | Random có seed, oscillator không bị aliasing, bộ lọc, tên cao độ, decibel |
| `src/sound/event.ts` | Những gì một nhạc cụ nhận vào và trả ra; glide (lướt) và vibrato (`pitchAt`) |
| `src/sound/instruments.ts` | Bộ đầu tiên (drums, bass, pad, pluck, riser, impact, whoosh, click), danh sách mọi type và giá trị mặc định của nó (`DEFAULTS`) |
| `src/sound/orchestra.ts` | Strings, brass, piano, electric piano, flute, bells, zither (đàn tranh), wobble bass, 8-bit pulse |
| `src/sound/ambience.ts` | Gió, mưa, room tone (tiếng phòng), suối, dế |
| `src/sound/effects.ts` | File thu sẵn (`sample`, có `measuredPeak`) và các effect preset |
| `src/sound/mix.ts` | Reverb, delay, ducking, limiter, đồng hồ đo loudness, file WAV |
| `src/sound/score.ts` | Định dạng score, các grid (`evenGrid`, `measuredGrid`), bước kiểm tra và render |
| `src/sound/voice.ts` | Phrase (cụm câu), thời gian từng từ, nhóm caption |
| `src/sound/cues-from-sim.ts` | Một ví dụ về mô phỏng có các sự kiện trở thành cue (mục 5.3) |

Engine, studio và công cụ capture không thay đổi gì vì việc này. File grid có cùng dạng với một grid đo được, file WAV được phục vụ từ `audio/` như mọi track, và chế độ video của công cụ capture mang theo `audioFile` của `src/project-config.ts`, được đặt là score khi score là nhạc của phim.

## 3. File score

`data/score.json` chứa toàn bộ score. Starter kèm một ví dụ nhỏ cho phim ví dụ của nó: 24 bar ở 120 BPM giọng La thứ (A minor), năm section khớp với các group của phim, và sáu cue.

| Khóa | Kiểu | Ý nghĩa |
|---|---|---|
| `tempo` | number | Số beat mỗi phút, cho toàn bộ score. Với một video giải thích (explainer), chủ phim này đã yêu cầu trên 130. Không dùng khi có `track` |
| `track` | `{file, gain, bus}` | Một track hoàn chỉnh để đặt score đè lên, một WAV có grid đã đo vào `data/audio.json` (mục 5.2). Tùy chọn |
| `seed` | number | Seed của mọi noise. Đổi nó để nghe noise khác, giữ nó để có cùng một file |
| `sampleRate` | number | Mặc định 48000 |
| `out` | path | File WAV, mặc định `audio/score.wav` |
| `tail` | giây | Âm thanh sau bar cuối, nơi reverb ngân hết; mặc định 1,5. Shot cuối được kéo dài tới đó. Khi có track, track quyết định độ dài |
| `master` | `{gain, lufs, ceiling}` | Gain tính bằng dB; mức loudness mục tiêu tính bằng LUFS (bản mix được chỉnh về đó trước limiter); trần của limiter tính bằng dBFS, mặc định -1 |
| `buses` | tên tới `{gain, reverb, delay, duck, key}` | Xem mục 6 |
| `duck` | `{attack, release, hold}` | Hình dạng của ducking, tính bằng giây |
| `reverb` | `{size, damp}` | Reverb dùng chung |
| `delay` | `{beats, feedback}` | Delay dùng chung; mặc định 0,75 beat (một nốt móc đơn chấm dôi) |
| `instruments` | tên tới `{type, bus, gain, pan, ...parameters}` | Xem mục 4 |
| `patterns` | tên tới `{bars, tracks}` | Các dòng bước hoặc nốt, mỗi nhạc cụ một dòng, lặp lại |
| `sections` | list các `{name, bars, play}` | Các phần của score, theo thứ tự. `play` liệt kê các pattern theo tên, hoặc dạng `{pattern, gain}`. Khi đè lên track có thể để rỗng |
| `cues` | list | Các sound effect của hình, mục 5 |
| `cueModules` | list các path | Các module tạo cue từ hình, mục 5.3 |
| `voice` | path | Voice-over, `data/voice.json`. Tùy chọn |

Tổng số bar của các section phải bằng độ dài của danh sách shot; script sẽ báo khi chúng khác nhau. Hãy viết các section theo các group của `shots.json`, để một lần chuyển phần trong câu chuyện cũng là một lần chuyển trong nhạc.

### Viết pattern

Một track của pattern là một dòng cho một nhạc cụ, cắt thành các bước đều nhau trải qua các bar của pattern.

| Loại nhạc cụ | Viết dưới dạng | Ví dụ |
|---|---|---|
| Trống, effect, bed, sample | Ký tự: `X` mạnh hết cỡ, `x` bình thường, `o` nhẹ, `.` nghỉ, `-` giữ bước trước. Dấu cách bị bỏ qua | `"X...x...x...x..."`: mười sáu bước, một tiếng kick trên mỗi beat |
| Có cao độ (`bass`, `pad`, `pluck` và mọi nhạc cụ của mục 4.2) | Các từ cách nhau bằng dấu cách: một nốt `A1`, một hợp âm `A3+C4+E4`, một glide `A1>C2`, `.` nghỉ, `-` giữ nốt trước, `A1:0.6` một độ mạnh | `". A1 . A1 . A1 . A1"`: tám bước, bass ở các phách nghịch (off-beat) |

Mười sáu bước một bar là nốt móc kép; tám là móc đơn; mười hai là chùm ba (triplet). Một pattern `bars: 4` với bốn hợp âm giữ mỗi hợp âm một bar. Một glide `A1>C2` trượt nốt đầu của bước sang nốt thứ hai trong suốt độ dài của nốt, hoặc trong `glide` giây khi nhạc cụ đặt giá trị đó; đàn tranh (zither) mặc định nhấn dây lên trong 0,18 giây, như người chơi guzheng làm sau khi gảy.

## 4. Các nhạc cụ

Mọi tham số đều có giá trị mặc định (`DEFAULTS` trong `src/sound/instruments.ts`); một nhạc cụ trong score chỉ ghi những gì nó thay đổi. Mỗi nhạc cụ render một phiên bản sạch của họ nhạc cụ đó, với chi phí thấp: không cái nào là bản thu, và không cái nào bắt chước một người chơi hay một sản phẩm cụ thể.

### 4.1 Bộ đầu tiên

| Type | Nó là gì | Tham số | Hit point |
|---|---|---|---|
| `kick` | Một sóng sin hạ cao độ, một chút drive, một tiếng click ngắn | `start`, `end` (Hz), `sweep`, `decay` (s), `click`, `drive` | Điểm bắt đầu |
| `snare` | Một tone ngắn và noise giới hạn dải | `tone`, `decay`, `noise`, `low`, `high` | Điểm bắt đầu |
| `clap` | Ba loạt noise và một đuôi | `centre`, `decay`, `spread` | Điểm bắt đầu |
| `hat` | Noise qua bộ lọc high-pass. `decay` dài hơn thì mở nó ra | `decay`, `tone` | Điểm bắt đầu |
| `bass` | Một sóng saw hoặc square giới hạn dải, một low-pass đóng lại sau mỗi nốt, một sóng sin thấp hơn một quãng tám | `shape`, `cutoff`, `env`, `fdecay`, `q`, `sub`, `attack`, `release`, `glide` | Điểm bắt đầu |
| `pad` | Ba sóng saw lệch tông mỗi nốt, trải sang trái phải, một low-pass nhẹ, attack chậm | `shape`, `detune` (cent), `cutoff`, `q`, `attack`, `release`, `width` | Điểm bắt đầu |
| `pluck` | `model: synth`, một sóng square qua bộ lọc đang đóng; hoặc `model: string`, một dây gảy (Karplus-Strong) | `model`, `shape`, `cutoff`, `env`, `fdecay`, `decay`, `damp`, `ring`, `glide` | Điểm bắt đầu |
| `riser` | Noise qua một dải tần đang leo lên, với một tone mờ, to dần | `from`, `to` (Hz), `q`, `tone` | **Điểm kết thúc**: nó leo lên vào sự kiện |
| `impact` | Một tiếng boom trầm hạ cao độ, với noise tối | `start`, `end`, `decay`, `noise`, `cutoff` | Điểm bắt đầu |
| `whoosh` | Noise qua một dải tần quét lên rồi quay lại, to nhất ở giữa | `from`, `peak`, `q` | **Điểm giữa**: nó lướt qua sự kiện |
| `click` | Một tiếng blip sin ngắn với một tick noise. Một nốt cho nó cao độ; `decay` dài hơn tạo ra tiếng ding | `pitch`, `decay`, `noise` | Điểm bắt đầu |

### 4.2 Nhạc cụ cho các yêu cầu "theo phong cách"

Tất cả đều có cao độ, chơi được hợp âm ở những họ có chơi hợp âm, glide được (`A1>C2`), và có hit point ở điểm bắt đầu.

| Type | Nó là gì | Tham số | Ghi chú |
|---|---|---|---|
| `strings` | Một bè dây: năm sóng saw lệch tông mỗi nốt, mỗi cái có vibrato chậm riêng, trải stereo, một low-pass mềm và một high-pass | `detune`, `cutoff`, `attack`, `release`, `depth` (vibrato, nửa cung), `glide` | `attack` dài cho các đoạn phồng lên (swell), ngắn cho marcato |
| `brass` | Hai sóng saw có bộ lọc mở ra khi nốt cất lên, với một cú hất nhẹ lên vào cao độ | `bright` (Hz), `attack`, `release`, `depth`, `glide` | Stab, swell, fanfare |
| `piano` | Mười hai partial (họa âm) hơi giãn, các partial cao tắt trước, hai giai đoạn decay, một tiếng búa, một bộ giảm âm khi nhả | `decay`, `release`, `inharmonic` | Rải hợp âm (arpeggio), hợp âm thưa |
| `epiano` | FM hai operator: một tiếng "bark" ở attack rồi dịu lại, một tiếng tine ngắn | `bark`, `decay`, `release` | Hợp âm mềm |
| `flute` | Một mô hình vật lý: một luồng hơi và một ống, theo sáo waveguide của Perry Cook, có tiếng hơi thở và vibrato | `breath`, `jet`, `noise`, `attack`, `release`, `depth`, `glide` | Đúng tông từ khoảng C4 tới C7: lệch trong 6 cent cho tới C6, thấp khoảng 25 cent ở E6 và G6. `breath` hoạt động trong khoảng 0,86 tới 0,92; dưới mức đó mô hình không phát tiếng, nên độ mạnh của nốt quyết định âm lượng chứ không phải hơi thở |
| `bell` | `model: bar`, một thanh kim loại đã chỉnh tông (glockenspiel, celesta) với bồi âm ở 2,76, 5,40 và 8,93; `model: church`, một chuông đúc (hum, prime, tierce, quint, nominal trên nốt) | `model`, `ring` | Thông báo, tiết lộ, kết thúc |
| `zither` | Một dây gảy có chiều dài theo cao độ, nên có thể nhấn nốt lên sau khi gảy, với vibrato chậm của guzheng, điểm gảy, và một thân gỗ nhỏ | `ring`, `bright`, `position`, `depth`, `glide` | Giai điệu ngũ cung có luyến (`E5>G5`) |
| `wobble` | Một sóng saw và một square thấp hơn một quãng tám qua một low-pass cộng hưởng được quét bởi một sóng chậm theo tempo | `beats` (độ dài một lần quét), `low`, `high` (Hz), `q`, `release`, `glide` | Dubstep và bass music; `beats: 0.5` rung theo móc đơn |
| `chip` | Một giọng pulse 8-bit: một xung độ rộng tùy chọn, âm lượng theo mười sáu nấc, hợp âm dạng arpeggio nhanh | `duty` (0.125, 0.25, 0.5), `arp` (số giây mỗi nốt của hợp âm), `decay`, `sustain`, `release`, `glide` | Game retro, pixel art |

Cao độ của mỗi nhạc cụ được đo trên bản render bằng phép tự tương quan (autocorrelation): strings, brass, piano, electric piano, bell, zither và chip lệch trong khoảng 6 cent so với nốt qua ba quãng tám; flute như đã nêu trên.

### 4.3 Lớp nền không khí (ambience bed)

Một bed kéo dài bằng sự kiện của nó: một cue có `beats`, hoặc một bước giữ bằng `-` trong pattern. Nó là stereo, nhỏ tiếng, và fade vào ra trong `fade` giây. Bus của nó là `bed` trừ khi nhạc cụ chỉ định bus khác.

| Type | Nó là gì | Tham số |
|---|---|---|
| `wind` | Noise mềm qua một dải tần có tâm lang thang, với những cơn gió chậm | `speed`, `low`, `high` (Hz), `q`, `fade` |
| `rain` | Một tiếng xì và nhiều giọt nhỏ, mỗi giọt một tiếng ping ngắn | `density` (số giọt mỗi giây), `hiss`, `fade` |
| `room` | Room tone: tiếng ù trầm tối và một chút không khí, với tiếng ù điện lưới tùy chọn | `hum` (Hz, 0 nếu không có), `fade` |
| `river` | Bốn dải noise sủi bọt ở tốc độ riêng của chúng | `fade` |
| `crickets` | Tối đa ba con côn trùng, kêu theo nhóm ba xung | `count`, `fade` |

### 4.4 Effect preset

Cho game, các màn tiết lộ phần thưởng, hoạt hình và giao diện. `note` của một cue dời một preset có cao độ tới nốt gốc đó. Mỗi preset có hit point ở đúng chỗ sự kiện thuộc về.

| Type | Nó là gì | Hit point | Tham số |
|---|---|---|---|
| `coin` | Hai nốt square nhanh cách nhau một quãng bốn | Nốt đầu | `root` |
| `fanfare` | Ba nốt brass lấy đà, rồi một hợp âm | **Hợp âm** | `root`, `step`, `hold` |
| `levelup` | Một arpeggio đi lên, rồi một hợp âm ngân có ánh lấp lánh | **Hợp âm** | `root`, `step` |
| `siren` | Một tiếng hú, hoặc hai tone (`mode: hilo`); kéo dài `beats` | Điểm bắt đầu | `low`, `high`, `period`, `mode` |
| `engine` | Các xung nổ theo tốc độ vòng tua, qua hai cộng hưởng ống xả, vòng tua tăng từ `from` tới `to` trong `beats` | Điểm bắt đầu | `from`, `to` (rpm), `cylinders` |
| `crunch` | Kim loại: một tá mode ngân vang bị đánh bởi một loạt tiếng lách tách, và một tiếng thịch | Điểm bắt đầu | `decay` |
| `pop` | Một bong bóng: một sóng sin quét lên trong 25 ms | Điểm bắt đầu | `from`, `to` |
| `boing` | Một lò xo hoạt hình: cao độ rung lắc rồi lắng xuống | Điểm bắt đầu | `root`, `decay` |
| `toggle` | Hai tiếng click nhỏ, xuống và lên | Điểm bắt đầu | |
| `success` | Hai nốt mềm đi lên một quãng năm | Điểm bắt đầu | `root` |
| `error` | Hai nốt trầm rè đi xuống | Điểm bắt đầu | `root` |
| `notify` | Ba nốt sáng, mỗi nốt có một chút tiếng chuông | Điểm bắt đầu | `root` |
| `key` | Một phím của bàn phím; mỗi phím hơi khác nhau | Điểm bắt đầu | |

Bộ đầu tiên bổ sung `click`, `whoosh`, `impact` và `riser` vào các preset này. Với một câu chuyện kể bằng âm thanh, pop, boing, whoosh và ding phủ được hầu hết hành động hoạt hình; foley của vật liệu thật (bước chân, vải, thủy tinh) thì nên dùng bản thu (mục 5.1).

### 4.5 Viết "theo phong cách" một tác phẩm có tên

Một yêu cầu có thể nêu tên một tác phẩm ("use the Oppenheimer theme as inspiration, but compose it yourself", "a song that would fit on Peter Gabriel's So"). Lấy phong cách của nó, không bao giờ lấy nội dung của nó.

| Lấy | Không lấy |
|---|---|
| Tempo, nhịp, cảm giác (thẳng, swing, dồn dập) | Giai điệu, hay bất kỳ câu nhạc nào mà người nghe gọi tên được |
| Điệu thức và màu hòa âm (thứ, modal, hợp âm chuyển chậm, nốt pedal) | Chuỗi hợp âm theo đúng thứ tự và tiết tấu của nó |
| Các họ nhạc cụ và vai trò của chúng (ostinato ở bè dây, brass phồng lên, một tiếng drone trầm) | Riff, hook, một đường bass dễ nhận ra |
| Kết cấu và mật độ, cách nó dồn lên, chỗ nó vỡ ra | Sample của bản thu, âm thanh của nó bị nhấc ra |
| Đặc điểm sản xuất (reverb lớn, trống khô và gần, snare có gate) | Lời bài hát, tựa đề, tên nghệ sĩ trên màn hình |

Hãy viết phong cách ra thành một tờ ngắn trước, mỗi hàng của cột bên trái một dòng, rồi xây score từ tờ đó, không phải từ trí nhớ về bản nhạc. Sau đó kiểm tra: hát giai điệu mới so với những gì bạn biết về bản gốc; nếu hai bar đầu của nó có thể bị nhầm là bản gốc, viết lại chúng. Nói với chủ phim rằng kết quả là theo phong cách của tác phẩm, và việc ngay cả điều đó có chấp nhận được cho mục đích sử dụng của họ hay không là câu hỏi của họ.

Điều giữ cho một score sạch:

| Làm | Vì sao |
|---|---|
| Một bè mỗi dải tần: kick và bass ở thấp, pad và pluck ở giữa, hat ở cao | Các bè chung dải tần làm nhòe lẫn nhau |
| Pad hoặc pluck, hiếm khi cả hai ở mức đầy | Hai bè hòa âm ở dải giữa làm track dày đặc |
| Bỏ trống ở chỗ cần đọc chữ, đưa trở lại ở drop | `music-and-beat.md`, mục 7. Score làm được điều mà một track có sẵn chỉ thỉnh thoảng làm được |
| Thay đổi gì đó ở mỗi section: một bè vào, một bè ra | Các phần của phim được nghe ra |
| Ít effect hơn số sự kiện | Một effect trên mọi sự kiện của một shot bận rộn là tạp âm. Đánh dấu các sự kiện mang ý tưởng |
| Một bed không khí rất nhỏ, hoặc không có dưới nhạc | Nó được cảm thấy, không phải được nghe thấy |

## 5. Sound effect: cue sheet

Một cue là một âm thanh gắn với một sự kiện của hình.

```json
{"at": {"shot": "steep-timer-rings", "beat": 4}, "sound": "ding", "note": "E6", "why": "The sand timer runs out and rings."}
```

| Trường | Ý nghĩa |
|---|---|
| `at` | Nơi hit point rơi vào: `{bar, beat}` đếm từ không như trong `shots.json`, hoặc `{shot, beat}` với beat đếm từ đầu shot, hoặc `{t}` tính bằng giây cho cue đến từ một mô phỏng (mục 5.3). Cho phép số lẻ |
| `sound` | Một nhạc cụ của score, hoặc một type trần (`impact`, `coin`, ...) với giá trị mặc định trên bus `sfx` |
| `gain` | dB |
| `vel` | Độ mạnh, 0 tới 1 |
| `beats` | Độ dài của một riser (đo ngược từ sự kiện), hoặc của một whoosh, siren, engine hay bed (đo tiếp từ sự kiện) |
| `note` | Cao độ của một âm có cao độ, hoặc nốt gốc của một preset |
| `pan` | -1 tới 1 |
| `why` | Sự kiện của hình mà nó đánh dấu. Renderer không đọc; nó dành cho lead và builder |

`{shot, beat}` là đồng hồ mà builder dùng trong shot (`sceneClock`, `kit-frame.ts`): một con dấu rơi vào `hit(k.beats, 4)` trong shot và một cue ở `{shot, beat: 4}` là cùng một khoảnh khắc. Hãy viết sự kiện vào brief của builder và cue vào score từ cùng một bảng của storyboard, để không cái nào phải đoán từ cái kia.

Một score đứng riêng ghi mọi sự kiện vào file grid dưới dạng một onset mang tên nhạc cụ, và các tiếng trống còn được ghi dưới `kick`, `snare` và `hat` như một track đo được. Vì vậy một shot có thể đọc `audio.hit('impact', t)` hoặc `audio.events('ding', t0, t1)` để phản ứng với một cue. Cue vẫn là nguồn; shot đặt hình của nó theo vị trí, không theo onset.

### 5.1 File thu sẵn, đặt theo đỉnh của chúng

Một nhạc cụ type `sample` phát một file WAV mà chủ phim chỉ định: từ một thư viện âm thanh, một thư mục của riêng họ, hoặc một bản thu.

```json
"crunch": {"type": "sample", "file": "audio/sfx/crunch.wav", "bus": "sfx"}
```

| Tham số | Ý nghĩa |
|---|---|
| `file` | File WAV, tương đối so với thư mục phim. Số nguyên 16 hoặc 24-bit hoặc float 32-bit, mono hoặc stereo, tần số lấy mẫu bất kỳ. Định dạng khác phải chuyển sang WAV trước, việc này cần một công cụ như ffmpeg: một việc nhẹ, nhưng vẫn cần chủ phim đồng ý nếu phải cài |
| `hit` | `peak` (mặc định): khoảnh khắc to nhất của file, đo trên các cửa sổ 5 ms (`measuredPeak` trong `src/sound/effects.ts`), để một tiếng click rơi đúng vào attack của nó và một whoosh rơi đúng vào đỉnh sóng; `start`: sample đầu tiên; hoặc một số giây tính từ đầu file |
| `root` | Nốt mà file phát ra. Khi có `root`, `note` của một cue phát file cao hơn hoặc thấp hơn bằng cách resample |

File mono được pan như mọi nhạc cụ mono; file stereo giữ hình ảnh âm thanh riêng của nó. File được đọc một lần và mỗi cue đặt nó lại. Đã thử với một file có đỉnh nằm ở 124 ms: đỉnh của nó rơi đúng vào beat của cue tới từng sample; một whoosh noise có đỉnh rộng rơi trong phạm vi 4 ms.

Bản quyền của mọi file là câu hỏi của chủ phim. Giữ nguồn và giấy phép chủ phim đưa ra bên cạnh các file, ví dụ trong một dòng `comment` của score, và không bao giờ tự ý tải effect từ web.

### 5.2 Đè lên một track hoàn chỉnh

Khi nhạc là một track chủ phim cung cấp hoặc đã mua, hãy đo grid của nó trước (`music-and-beat.md`, mục 4 và 5). Sau đó một score có `track` đặt các effect, một giọng hoặc một bed đè lên nó:

```json
{"track": {"file": "audio/track.wav", "gain": -3}, "out": "audio/mix.wav",
 "master": {"lufs": -14, "ceiling": -1},
 "buses": {"track": {"duck": 5}, "sfx": {"key": true}},
 "instruments": {"crunch": {"type": "sample", "file": "audio/sfx/crunch.wav", "bus": "sfx"}},
 "patterns": {}, "sections": [],
 "cues": [{"at": {"bar": 8}, "sound": "crunch", "why": "The car hits the wall."}]}
```

| Chuyện gì xảy ra | Như thế nào |
|---|---|
| Grid | Đọc từ `data/audio.json`, grid mà bước phân tích đã đo, các beat trước downbeat đầu tiên được tính là pickup. Script từ chối grid do chính một score soạn ra. Các vị trí tính bằng bar và beat đi theo các beat đo được, kể cả chỗ trôi nhịp (`measuredGrid` trong `src/sound/score.ts`) |
| Track | Được mix trên bus riêng, là `track` trừ khi `track.bus` chỉ định bus khác, để có thể duck nó: dưới giọng nói, hoặc dưới các effect trên một bus được đánh dấu `key` |
| Loudness | Toàn bộ bản mix, kể cả track, được chỉnh về `master.lufs` và qua limiter |
| File grid | Giữ nguyên. Caption của giọng vẫn được ghi |

Đặt `audioFile` trong `src/project-config.ts` là bản mix khi đó là thứ phim phát. Đã thử trên một grid trôi từ 120 lên 126 BPM với pickup hai beat: các tiếng kick được score đặt trên grid đó bắt đầu trong phạm vi 0,01 ms so với các beat đo được ở bar 0, 5, 11, 17 và 23.

### 5.3 Âm thanh từ hình

Một số phim tạo âm thanh từ những gì hình làm: "every note comes from a visible collision" ("mỗi nốt đến từ một va chạm nhìn thấy được"), tiếng lách tách của ngọn lửa từ độ sáng của nó. Khi đó hình là nguồn và âm thanh đi theo. Các sự kiện đến từ một mô phỏng, và mô phỏng phải là một hàm thuần (pure function) duy nhất mà cả shot và score đều chạy.

| Phần | Quy tắc |
|---|---|
| Mô phỏng | Một module không import DOM hay Node, không đồng hồ và không random thiếu seed, tích phân với bước cố định, trả về các sự kiện kèm thời gian của chúng. Nó nằm ở chỗ cả hai đều import được: `src/sound/` hoặc `src/scenes/parts/` |
| Shot | Chạy nó một lần trong `init()` và vẽ từ kết quả tại `f.t` |
| Score | Ghi tên module trong `cueModules`. Module export `cues(ctx)`, nhận danh sách shot và grid (`CueContext` trong `src/sound/score.ts`) và trả về các cue, thường với `at: {t}` |
| Một sự kiện nằm giữa hai bước | Được tìm bằng nội suy bên trong bước, để âm thanh rơi đúng chỗ va chạm xảy ra, không phải ở bước kế tiếp |
| Một đại lượng liên tục (độ sáng, tốc độ) | Chuyển thành sự kiện: nhiều cue nhỏ có mật độ hoặc độ mạnh theo nó, hoặc một bed có `gain` thay đổi theo section |

`src/sound/cues-from-sim.ts` là một ví dụ hoàn chỉnh: một quả bóng thả ở downbeat của bar 2 nảy lên, và mỗi lần chạm đất trở thành một tiếng chuông leo lên một thang âm, to hơn khi bóng nhanh hơn. `simulateBall` và `ballAt` của nó là những gì một shot sẽ gọi. Chỉ các âm thanh đến từ hình mới dùng `{t}`; nhạc vẫn ở trên grid.

### 5.4 Hình từ score

Chiều ngược lại: nhạc được soạn trước, và hình làm cho mọi nốt nhìn thấy được, như trong "a machine that plays a piece of music, every note a visible collision" ("một cỗ máy chơi một bản nhạc, mỗi nốt là một va chạm nhìn thấy được"). Khi đó score là nguồn và hình đi theo nó.

| Phần | Như thế nào |
|---|---|
| Các sự kiện | Một scene đọc chính các sự kiện của score, không bao giờ đọc một danh sách gõ lại: `scoreEvents(score, shots, grid)` trong `src/sound/score.ts` là hàm thuần, và cùng với `evenGrid(tempo, bars)` nó cho nhạc cụ, thời gian tính bằng giây, cao độ và độ mạnh của mọi nốt. Scene import `data/score.json` (`import score from '../../data/score.json'`, cách này chạy được trong studio và trong file đơn), hoặc fetch nó trong `init()` |
| Chuyển động | Lên kế hoạch ngược từ mỗi sự kiện: đường bay của quả bóng, cú vung của cái búa, cú rơi của quả nặng là một hàm giải tích chạm tới mục tiêu đúng vào thời điểm của nốt. Thời điểm phóng và tốc độ suy ra từ mục tiêu và lúc tới nơi |
| Kiểm tra | Các still ở sự kiện của mỗi nhạc cụ và một frame ở mỗi bên: điểm chạm rơi đúng vào frame của sự kiện. Và mọi sự kiện đều ở trong khung hình vào thời điểm của nó: chiếu mỗi cú đánh qua camera tại frame của nó (`screenPoint(cam, p)` và `inFrame(cam, p, margin, within)` trong `src/scenes/parts/kit-camera.ts`, cho camera phẳng, camera 3D hoặc camera three.js). Từ thực tế: ở lần chạy đầu tiên của bước kiểm tra đó, 22 trong số 332 cú đánh của một phim thử nằm ngoài khung hình, và các chuyển động camera đã được thay đổi |

Ai viết score: lead, như khi viết storyboard, vì chủ phim đánh giá nhạc bằng tai và duyệt nó trước khi dựng bất cứ thứ gì. Builder có thể đề xuất thay đổi trong báo cáo của mình, như mọi thay đổi nằm ngoài các file của nó. Từ thực tế: với cỗ máy va chạm, lead viết một score chỉ gồm nhạc cụ gõ và gảy (mỗi nốt cần một cú đánh nhìn thấy được, nên không có pad ngân), chủ phim duyệt bằng tai, và một builder dựng cỗ máy từ các sự kiện của nó trong một vòng.

## 6. Bản mix

| Tầng | Nó làm gì | Đặt ở đâu |
|---|---|---|
| Nhạc cụ | Gain và pan của mỗi âm thanh | `instruments.<name>.gain`, `pan` |
| Bus | Gain của một nhóm: mặc định `drums` (kick, snare, clap, hat), `bass` (bass, wobble), `music` (mọi nhạc cụ có cao độ khác), `bed` (ambience), `sfx` (effect, sample), `voice`, và `track` | `buses.<name>.gain` |
| Send | Một phần của bus được gửi tới reverb dùng chung và delay dùng chung | `buses.<name>.reverb`, `delay` (0 tới 1) |
| Ducking | Các bus có `duck` hạ xuống ngần ấy dB trong khi một bus có `key` đang phát. Bus giọng mặc định là một key; đánh dấu `sfx` là key để hạ track dưới các cú hit. Cú hạ bắt đầu `attack` giây trước key, vì toàn bộ file đã biết trước, và các khoảng hở ngắn hơn `hold` không để bed trồi lên lại giữa các từ | `buses.<name>.duck`, `key`; `duck` |
| Master | Gain, rồi mức loudness mục tiêu, rồi một limiter look-ahead ở mức trần, rồi một fade qua phần tail | `master` |

Script in ra integrated loudness của kết quả (BS.1770, có gating), sample peak của nó, và mức giảm lớn nhất của limiter kèm thời điểm. Một limiter cắt hơn khoảng 6 dB ở một khoảnh khắc là đang làm bẹp nó: hạ bus đang to ở đó, hoặc hạ mục tiêu. Loudness được đo trước limiter và chỉnh về mục tiêu, rồi limiter cắt bớt một chút, nên kết quả rơi hơi dưới mục tiêu. Peak là sample peak, không phải true peak.

Các mục tiêu phổ biến: khoảng -14 LUFS cho hầu hết nền tảng streaming và mạng xã hội. Hãy hỏi phim sẽ được chiếu ở đâu. Giữ effect dưới nhạc trừ khi effect chính là sự kiện.

## 7. Âm thanh đi về đâu

| File | Dùng cho |
|---|---|
| `audio/score.wav` | Studio phát nó: `src/project-config.ts` liệt kê nó trong `studioAudio` dưới nhãn `score`, nên công tắc nhạc đưa ra lựa chọn này khi file tồn tại. Khi score là nhạc của phim, đặt luôn `audioFile` là nó, để bản export mang theo nó |
| `data/audio.json` | Được ghi bởi score đứng riêng: `beats`, `downbeats`, thời gian shot (từ `shots.json`, rồi được build script ghi lại), `features` (`rms` của bản mix; `low`, `mid`, `high` và, khi có giọng, `vocal`, là tổng các nhạc cụ của chính score theo dải tần), `onsets`, và `notes` với `grid_source: composed`, các con số loudness và limiter. Một score đè lên track thì để yên file này |
| `data/lyrics.json` | Các nhóm caption của voice-over, mục 11 |

Một file WAV 48 kHz stereo khoảng 11 MB mỗi phút. Studio phát nó nguyên trạng. Một bản nén cho studio là tùy chọn; nó phải giữ đúng định thời.

## 8. Chạy và kiểm tra

```sh
bun run score -- --check     # the faults, or what would be made
bun run score                # the WAV, the grid, the captions
bun run shots
bun run score -- --score <file> --no-grid   # another score file, the WAV only
```

| Kiểm tra | Cách làm | Đạt khi |
|---|---|---|
| Tất định | Chạy `bun run score` hai lần và so checksum của file WAV, `data/audio.json` và `data/lyrics.json` (`sha256sum` trong Git Bash hoặc trên macOS và Linux, `Get-FileHash` trong PowerShell) | Chúng bằng nhau |
| Đúng nhịp | Phát studio với công tắc nhạc ở `score`, rồi ở `click`, tại cùng một khoảnh khắc | Tiếng click và tiếng kick là một |
| Sự kiện của hình | Xem khoảnh khắc của mỗi cue trong studio | Âm thanh rơi đúng vào sự kiện, không phải gần đó |
| Bản mix | Các con số loudness, peak và limiter được in ra | Trong mục tiêu; limiter dưới khoảng 6 dB |
| Gu | Chủ phim nghe | Chủ phim nói vậy |

Đo trên một máy Windows 11 ngày 2026-09-28, bun 1.4.2: score ví dụ (48 kHz stereo, 49,5 giây, 280 âm thanh và bốn phrase giọng) render trong 2,5 tới 2,9 giây trên một nhân, và ba lần chạy cho ra file giống nhau từng byte. Các pad chiếm phần lớn thời gian đó; các demo khác render trong 0,4 tới 2,8 giây. `Math.sin`, `Math.exp` và `Math.tan` không được đặc tả chính xác tới bit cuối giữa các JavaScript engine, nên một file tạo trên hệ thống khác hoặc phiên bản bun khác có thể khác ở các bit thấp nhất; grid và thời gian sự kiện thì không.

`--no-grid` chỉ ghi file WAV và để nguyên `data/audio.json` và `data/lyrics.json`: dùng cho một bài thử, một demo, hoặc một phiên bản âm thanh thứ hai để so bằng tai.

## 9. Giọng đọc: lấy từ đâu

| Nguồn | Rời khỏi máy | Chi phí | Thời gian từng từ | Ngôn ngữ | Trạng thái ở đây |
|---|---|---|---|---|---|
| Giọng Windows qua SAPI (`System.Speech`), `scripts/voice-sapi.ps1` | Không | Không tốn gì | Điểm bắt đầu từ, do engine cung cấp | Những giọng đã cài. Một Windows 11 tiếng Anh nguyên bản có Microsoft David và Zira, chỉ tiếng Anh | Đã chạy trên Windows 11 ngày 2026-09-28 |
| `say` của macOS | Không | Không tốn gì | Không rõ có; ước lượng (mục 10) | Những giọng đã cài | Chưa chạy. Lệnh là `say -v <voice> -o <file>.wav --data-format=LEI16@22050 "<text>"` |
| Piper, một giọng neural chạy local | Không | Không tốn gì, nhưng phải cài | Chưa xác nhận có; ước lượng | Theo từng model giọng tải về | Chưa chạy. Cài nó cần chủ phim đồng ý |
| edge-tts, một package Python | **Có**: văn bản được gửi tới dịch vụ đọc to trực tuyến của Microsoft | Không tốn gì | Ranh giới từ khi được yêu cầu (`boundary="WordBoundary"`; mặc định của nó là ranh giới câu) | Nhiều, có tiếng Việt | Chưa chạy. Nó gửi kịch bản ra ngoài và dùng một dịch vụ không có hợp đồng; hãy hỏi |
| Giọng trả phí (ElevenLabs, Azure, Google, OpenAI và các hãng khác) | Có | Có | Một số trả về thời gian, một số không; đọc tài liệu của họ | Nhiều | Chưa chạy. Hãy hỏi, kèm chi phí |
| Giọng người thật do chủ phim thu | Không | Không tốn gì | Cần một công cụ transcription (phiên âm) hoặc forced alignment (căn chỉnh cưỡng bức), tức là phải cài | Bất kỳ | Chưa xây (mục 10) |

Nói với chủ phim cái nào gửi văn bản đi và cái nào tốn tiền, và để chủ phim chọn. Một phim tiếng Việt cần giọng tiếng Việt: không giọng Windows local nào đã thử nói được tiếng Việt, nên hãy hỏi chủ phim, từng phim một, dùng giọng nào.

Những gì phát hiện được với SAPI: engine báo điểm bắt đầu của mọi từ, tính bằng giây của file nó ghi, qua các sự kiện tiến trình (progress event). Nó không báo điểm kết thúc. Với các giọng desktop đã thử, các thời gian đó được tính như thể file được ghi ở 16 kHz: khi ghi ở 24 kHz, mọi thời gian đều trễ gấp 1,5 lần. Vì vậy script ghi file 16 kHz. Kiểm tra với âm thanh của file, các điểm bắt đầu từ sau một khoảng ngừng lệch trong khoảng 10 ms. Hai lần chạy cho ra file giống nhau.

## 10. Giọng đọc: dữ liệu và đồng hồ

### Đồng hồ nào cai quản

Beat grid vẫn cai quản. Mỗi phrase của giọng được đặt vào một vị trí trên grid: từ đầu tiên của nó rơi đúng vào bar và beat mà lead ghi. Bên trong một phrase, các từ giữ thời gian mà giọng đọc đã cho chúng. Nhờ vậy các cú cắt vẫn ở trên downbeat, đồng hồ của builder vẫn tính bằng beat, và giọng được đặt lên nhạc như cách đặt một shot. Trên một track đã đo, điều tương tự vẫn đúng, trên các beat đo được.

| Vấn đề | Quy tắc |
|---|---|
| Một phrase | Một câu, hoặc một nhóm hơi của một câu dài. File riêng, vị trí riêng |
| Bắt đầu ở đâu | Trên một beat, thường là beat thứ nhất hoặc thứ hai sau cú cắt của shot mà nó đọc đè lên. `{shot, beat}` nói thẳng điều đó |
| Được dài bao lâu | Tới phrase kế tiếp. Script cảnh báo khi một phrase chạy lấn vào phrase sau. Một phrase mười từ mất khoảng bốn giây, hai bar ở 120 BPM |
| Cú cắt | Trên downbeat như trước. Một phrase có thể chạy qua một cú cắt; một phrase bắt đầu ngay trước một cú cắt nghe như bị trễ |
| Nhạc | Một bed, được duck dưới giọng (mục 6). Bỏ trống dưới những câu dài nhất |
| Nhịp độ | Khoảng hở giữa các phrase đến từ grid, một hoặc hai beat. Quá nhiều khoảng hở làm giọng nghe như bị bậc thang: khi đó hãy viết phrase dài hơn, hoặc đặt một phrase ở phách nghịch (`beat: 1.5`) |

Chiều ngược lại, một grid bị uốn theo một giọng được thu liền một mạch, thì chưa được xây: nó cần thời gian của các từ trong bản thu, thứ chỉ một công cụ transcription hoặc alignment mới cho được, và cần cắt bản thu thành các phrase. Khi có những thời gian đó, các phrase có thể được cắt ra và đặt theo cùng cách.

### Các file

`data/voice.json`, do lead viết:

```json
{
  "voice": {"engine": "sapi", "name": "Microsoft Zira Desktop", "rate": 0},
  "captions": {"maxWords": 5, "maxChars": 26, "gap": 0.3, "lead": 0.05, "hold": 0.5, "min": 0.7},
  "phrases": [
    {"id": "v01", "text": "Boiling water on green leaves | turns the cup bitter.", "at": {"bar": 2, "beat": 1}},
    {"id": "v03", "text": "Three minutes, | then lift them out.", "at": {"shot": "steep-colour-spreads", "beat": 0}}
  ]
}
```

| Trường | Ý nghĩa |
|---|---|
| `phrases[].id` | Đặt tên cho file `audio/voice/<id>.wav` |
| `phrases[].text` | Những gì được nói. `\|` kết thúc một nhóm caption, `/` ngắt dòng bên trong một nhóm; cả hai đều không được đọc ra |
| `phrases[].at` | Nơi từ đầu tiên rơi vào |
| `phrases[].gain` | dB, cho một phrase bị ra nhỏ hơn |
| `voice` | Cho bước giọng: engine, tên giọng, tốc độ (SAPI: -10 tới 10) |
| `captions` | Quy tắc nhóm chữ, mục 11 |

`data/voice-words.json` được ghi bởi bước giọng, không bao giờ viết tay: với mỗi phrase là file của nó, độ dài, `timing` (`engine` hoặc `estimated`) và các từ của nó với điểm bắt đầu và kết thúc tính bằng giây của file đó. Bất kỳ bước giọng nào ghi ra file này và các file WAV đều chạy được với phần còn lại, dù nó điều khiển engine nào.

Sau đó `bun run score` lấy thời gian của mỗi từ từ voice engine khi engine cho đúng một thời gian cho mỗi từ của văn bản, và kéo điểm kết thúc của mỗi từ lùi về chỗ âm thanh của nó dừng. Khi không có thời gian, hoặc chúng không khớp với các từ của văn bản, nó ước lượng: phần lời nói giữa âm thanh đầu và cuối được chia theo số âm tiết của mỗi từ, thêm một chút sau dấu câu. Thời gian ước lượng được đánh dấu `estimated` trong đầu ra. So với thời gian SAPI của ví dụ, chúng lệch tới một phần tư giây: đủ tốt cho các nhóm vài từ, không đủ để sáng lên từng từ một.

Viết cho giọng đọc: khoảng hai từ rưỡi mỗi giây; sáu mươi giây là khoảng một trăm năm mươi từ. Đọc to mọi phrase ở nhịp độ đó trước khi đặt nó. Các câu của giọng đọc cũng là các câu trên màn hình, nên các quy tắc của `type-and-captions.md`, mục 3, áp dụng cho chúng.

## 11. Caption từ giọng đọc

`bun run score` ghi các nhóm caption vào `data/lyrics.json`, theo dạng mà `src/engine/lyrics.ts` đọc, nên mọi scene đều có chúng dưới dạng `this.ctx.lyrics`. Mỗi nhóm là một dòng của file đó, với `text`, `start` và `end` (khi nào nó ở trên màn hình, theo thời gian bài nhạc), `rows` (các dòng của nó trên màn hình), `phrase` (id phrase của nó) và `words` (mọi từ với điểm bắt đầu và kết thúc khi được nói). Một bản của file này do script ghi sẽ bị xóa khi score không còn giọng đọc.

Cách nhóm các từ:

| Quy tắc | Mặc định |
|---|---|
| Ở chỗ lead đã viết `\|` trong một phrase, chỉ riêng các dấu đó quyết định các nhóm của phrase đó | Ngắt theo nghĩa, như `type-and-captions.md`, mục 4 yêu cầu |
| Ở chỗ khác, một nhóm kết thúc sau dấu câu, trước một khoảng lặng `gap` giây, và trước khi nó vượt quá `maxWords` từ hoặc `maxChars` ký tự | 0,3 s, 5 từ, 26 ký tự |
| Một nhóm xuất hiện `lead` giây trước từ đầu tiên của nó | 0,05 s |
| Nó ở lại `hold` giây sau từ cuối cùng, tổng cộng ít nhất `min` giây, nhưng không bao giờ quá điểm bắt đầu của nhóm kế tiếp | 0,5 s, 0,7 s |

Nhóm từ hai tới sáu từ hợp với lời nói: hai hoặc ba cho nhịp cắt sôi động, tới sáu cho phần giải thích điềm tĩnh.

### Overlay vẽ chúng như thế nào

Caption in cứng (burned-in) ở chân khung hình là lựa chọn bình thường cho một phim dẫn dắt bằng giọng: phần lớn người xem tắt tiếng, và chữ phải đi theo giọng. Overlay của starter (`src/scenes/overlay.ts`) vẽ mọi nhóm caption của giọng lên mọi shot, kể cả thẻ tiêu đề và thẻ kết:

| Vấn đề | Như thế nào |
|---|---|
| Những dòng nào | Các dòng của `data/lyrics.json` có mang id `phrase`. Lời hát không có, và được để cho các shot của một lyric film (phim lời bài hát) |
| Ở đâu | Một viên thuốc (pill) căn giữa vùng caption (`CAPTION` trong `kit-frame.ts`), đứng trên cạnh dưới của vùng đó, bên trong vùng an toàn |
| Look | Một pill màu mực đục với các dòng ở sentence voice (kiểu chữ cho câu), không nhãn và không thanh accent, để nó không bao giờ bị nhầm là plate của storyboard. Kích thước khớp với dòng rộng nhất, từ 58 px xuống 40 px ở bề rộng 1080 |
| Định thời | Hiện từ `start` của nhóm tới `end` của nó, đọc theo thời gian riêng của frame, với fade 0,06 giây |
| Chữ | Các từ chưa được nói được vẽ ở nửa độ đậm và mỗi từ sáng lên khi nó được nói, theo thời gian từng từ. `VOICE.dim` ở đầu overlay đặt điều này; giá trị 1 hiện mọi từ như nhau |
| Trên nền tối | Pill có một viền mờ, để nó giữ được hình dạng |

Một plate của storyboard đặt ở dưới trong lúc caption giọng đang hiện sẽ nằm đè lên nó. Overlay đẩy plate đó lên trên trong suốt thời gian giọng nói, và `bun run score` cảnh báo kèm section và bar của plate và chữ của caption, để storyboard được sửa lại cho đúng: chuyển plate lên trên hoặc ra giữa, hoặc để giọng mang câu đó. Plate thay thế của một thẻ cũng được đẩy lên theo cùng cách.

Đã kiểm tra trên bốn still của phim ví dụ trên Windows 11 ngày 2026-09-28, với giọng ví dụ do SAPI đọc. Ở 5,3 giây pill hiện "Boiling water on" sáng và "green leaves" mờ, và ở 41,9 giây, trên thẻ kết, "mind" sáng và "the time." mờ, cả hai đều khớp thời gian từng từ. Ở 9,6 và 25,6 giây, một plate dưới và một plate thay thế ban đầu đã đè lên pill; với quy tắc trên, chúng đứng ở trên.

Những gì `type-and-captions.md` nói vẫn đúng: vùng an toàn, kích thước tối thiểu, plate đục, chữ dưới ngưỡng bloom. Điều thay đổi khi có giọng là định thời: một nhóm hiện trong suốt thời gian nó được nói, không phải trong thời gian cần để đọc, nên một câu cần được đọc trọn vẹn thì thuộc về một plate riêng, giữ trong một khoảng ngừng của giọng.

## 12. Cái gì đã chạy và cái gì chưa

| Hạng mục | Trạng thái |
|---|---|
| `bun run score` trên score ví dụ, có và không có giọng, `--check`, một score có lỗi, `--no-grid` | Đã chạy trên Windows 11, 2026-09-28. Giống nhau từng byte qua ba lần chạy; các onset kick trong file lệch trong một sample so với grid. Các bổ sung của vòng hai giữ nguyên đầu ra của ví dụ tới từng byte |
| File thu sẵn đặt theo đỉnh đo được, đè lên một track trên grid đo được bị trôi, track được duck dưới các effect, bản mix ở -14 LUFS | Đã chạy trên Windows 11, 2026-09-28, với các file thử tạo bằng code, không phải với thư viện thật hay track thật. Hai lần chạy giống nhau |
| Các nhạc cụ của mục 4.2, các bed, các preset, glide | Đã render trên Windows 11, 2026-09-28; cao độ đo như trong mục 4.2; mức âm lượng đã đo. **Chưa nghe** |
| Cue từ một mô phỏng (`src/sound/cues-from-sim.ts`) | Đã chạy: năm lần va chạm, lần đầu ở đúng thời điểm mà rơi tự do cho ra |
| `bun run voice:sapi` với Microsoft Zira | Đã chạy trên Windows 11, 2026-09-28. Điểm bắt đầu từ được kiểm tra với âm thanh của file. Giống nhau qua hai lần chạy |
| Caption giọng do overlay vẽ | Đã xem bốn still, trên Windows 11, 2026-09-28 |
| Nghe | **Chưa làm.** Lead không thể nghe kết quả. Mọi nhạc cụ, giá trị mặc định và demo đều chưa được kiểm tra bằng tai |
| Score trong studio, trên trình duyệt của chủ phim | Chưa chạy |
| `say` của macOS, Piper, edge-tts, giọng trả phí, transcription, forced alignment | Chưa chạy |
| Tổng hợp trực tiếp trong trang (Web Audio), đọc trực tiếp MP3 hoặc định dạng khác | Chưa xây |
| Export một video mang theo score | Chưa chạy (không export video khi chưa có lời của chủ phim) |

## 13. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Công tắc nhạc không có `score` | File WAV chưa được tạo, hoặc `studioAudio` không liệt kê nó | Chạy `bun run score`; giữ mục `score` trong `src/project-config.ts` |
| Các shot bắt đầu sai thời điểm sau một score mới | Score đã đổi tempo hoặc số bar, và thời gian shot chưa được ghi lại | Chạy `bun run shots` sau mỗi lần làm score |
| Script cảnh báo score và danh sách shot khác nhau về số bar | Các section của score cộng lại không bằng phim | Làm cho chúng bằng nhau |
| Một riser nghe thấy trước chỗ nó được viết | Hit point của nó là điểm kết thúc, trong pattern cũng như trong cue: nó tới nơi ở bước của nó | Viết riser và whoosh dưới dạng cue `at` sự kiện, với `beats` cho độ dài của chúng |
| Một effect thu sẵn rơi trễ | Hit point của nó được đặt là `start`, và file có khoảng lặng hoặc attack chậm trước đỉnh | Để `hit` ở `peak`, hoặc đưa số giây của khoảnh khắc thuộc về sự kiện |
| Script từ chối grid của một track | `data/audio.json` chứa grid do một score soạn ra, không phải của track | Đo track (`music-and-beat.md`, mục 4) |
| Effect trôi lệch khỏi track về cuối | Chúng được đặt trên một grid đều theo tempo của track | Dùng `track`, thứ đọc grid đo được |
| Một file sample bị từ chối | Nó không phải WAV | Chuyển nó sang WAV trước, với sự đồng ý của chủ phim nếu phải cài công cụ |
| Sáo không phát tiếng, hoặc rít lên | `breath` nằm ngoài 0,86 tới 0,92, hoặc một nốt dưới khoảng C4 | Giữ `breath` trong khoảng đó; giao nốt trầm cho strings hoặc pluck |
| Một score "theo phong cách" nghe giống bản gốc | Giai điệu hoặc hợp âm của nó đã bị lấy | Viết lại từ tờ phong cách (mục 4.5) |
| Mọi thời gian từ đều trễ gấp 1,5 lần | Một file SAPI ghi ở 24 kHz | Dùng `scripts/voice-sapi.ps1`, script này ghi 16 kHz |
| Các từ bị đánh dấu `estimated` với giọng SAPI | Engine báo số từ khác với số từ trong văn bản (số, chữ viết tắt) | Viết số và chữ viết tắt ra thành chữ trong văn bản |
| Một phrase giọng không có trong bản mix | File WAV của nó không tồn tại; script có báo | Chạy bước giọng |
| Một plate nhảy lên trên trong lúc giọng nói | Nó được đặt ở dưới, chỗ caption giọng đứng; script có cảnh báo | Đặt nó ở trên hoặc giữa trong `shots.json` |
| Nhạc bị "bơm" (pumping) giữa các từ | `hold` ngắn hơn các khoảng ngừng trong lời nói | Tăng `duck.hold` |
| Drop nghe bẹp | Limiter cắt mất vài dB ở đó | Hạ impact hoặc bus đang đạt đỉnh ở đó; đọc thời điểm script in ra |
| Bản mix dày đặc | Quá nhiều bè ở dải giữa | Bỏ một bè (mục 4.5) |
| File khác ở các bit cuối trên một máy khác | Các hàm toán học khác nhau giữa các engine | Bình thường. So sánh trên cùng một máy |
| Chủ phim nghe thấy văn bản kịch bản của mình trong dịch vụ của một công ty | Đã dùng một giọng cloud mà không hỏi | Hỏi trước khi dùng bất kỳ giọng nào rời khỏi máy |
