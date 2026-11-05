# Storyboard

Storyboard (bảng phân cảnh) là bộ phim được viết ra dưới dạng dữ liệu trước khi vẽ bất kỳ hình nào: mỗi shot (cảnh quay) cùng vị trí của nó trong nhạc, và mỗi câu chữ người xem sẽ đọc. File này mô tả schema của dữ liệu đó, các bước kiểm tra nó phải vượt qua, những gì được sinh ra từ nó, và cách lead (người dẫn dắt) viết, định hình và thay đổi nó.

Đọc file này khi: bạn viết hoặc sửa danh sách shot hay file copy (câu chữ), chạy generator (bộ sinh), chuẩn bị animatic cho chủ phim, chọn id cho shot, hoặc thay đổi thứ tự hay nội dung của một bộ phim mà các shot đã tồn tại.

Các đường dẫn trong file này là tương đối so với một thư mục phim được tạo từ `assets/starter/`.

## 1. Vì sao storyboard là dữ liệu

Một storyboard viết bằng văn xuôi phải được chép tay vào mọi chỗ cần đến nó, và các bản chép sẽ lệch nhau dần. Viết dưới dạng dữ liệu, nó là nguồn duy nhất cho ba thứ.

| Sản phẩm | Ai dùng | Nó lấy gì từ dữ liệu |
|---|---|---|
| Tài liệu storyboard | Chủ phim đọc và sửa. Builder (người dựng) đọc trước khi dựng | Mọi trường của mọi shot, các câu chữ, các lý do |
| Ranh giới thời gian của các shot | App, để biết shot nào chạy lúc nào | `id`, `bar`, `bars`, và beat grid (lưới phách) |
| Các thẻ của animatic | Chủ phim, người xem chúng trong studio cùng với nhạc | Các trường mô tả của mỗi shot, được app đọc lúc chạy |

- Lead sửa hai file dữ liệu. Mọi thứ khác đều được sinh ra từ chúng hoặc đọc trực tiếp từ chúng.
- App không giữ bản sao nào về việc một shot là gì hay một caption (phụ đề/chữ trên hình) nói gì.
- Generator chạy sau mỗi thay đổi ở bất kỳ file nào trong hai file, và các bước kiểm tra của nó phải đạt trước khi ai đó bắt tay dựng.

## 2. Hai file và schema của chúng

| File | Chứa |
|---|---|
| `shots.json` | Các loại transition (chuyển cảnh), các group (các phần của phim), các shot, các caption |
| `copy.json` | Mọi câu chữ của phim, đã ngắt sẵn thành dòng, và các nhãn nhỏ trên plate (tấm nền chữ) |

Các tên dùng trong cột "Được đọc bởi": generator là `scripts/build-shot-files.py`; app là `src/film.ts` và `src/timeline.ts`; card (thẻ) là `src/scenes/storyboard-card.ts`; overlay (lớp phủ) là `src/scenes/overlay.ts`; studio là trang do `src/main.ts` tạo ra. App đọc cả hai file qua `src/film.ts`, file này cũng cung cấp kiểu (type) của chúng. Trong toàn bộ starter, một bar (ô nhịp) có bốn beat (phách). Bar là bar của nhạc, đếm từ số không, và có thể là số lẻ.

"Bắt buộc" nghĩa là generator từ chối dữ liệu nếu thiếu nó. Mọi trường đều mang tính tổng quát: starter không có trường nào chỉ thuộc về riêng một bộ phim.

### Danh sách shot, cấp trên cùng

| Trường | Kiểu | Ý nghĩa | Được đọc bởi |
|---|---|---|---|
| `comment` | string | Các quy ước của file, viết bằng văn xuôi | Chỉ con người |
| `transitions` | object, loại tới `{label, what}`, bắt buộc | Từ điển các loại transition: một cái tên và một mô tả cho tài liệu. Mỗi loại phải là loại mà engine có thể chạy | Generator, card |
| `groups` | array, theo thứ tự phim, bắt buộc | Các phần của phim | Generator, overlay, studio |
| `shots` | array, theo thứ tự phát, bắt buộc | Các shot. Các bước kiểm tra so sánh các shot liền kề theo thứ tự này | Generator, app, card, overlay, studio |
| `captions` | array, bắt buộc (có thể rỗng) | Khi nào và bằng cách nào mỗi câu đến với người xem | Generator, overlay, builder qua `captionFor` trong `src/film.ts` |

### Group (một phần)

| Trường | Kiểu | Ý nghĩa | Được đọc bởi |
|---|---|---|---|
| `id` | string, bắt buộc, duy nhất | Khóa mà các shot, caption và file copy tham chiếu tới | Generator, app, overlay, studio |
| `kind` | `title`, `section`, `recap` hoặc `end`, bắt buộc | Group đó là gì. Chỉ `section` mới mang bộ đếm, caption và copy | Generator, overlay, studio |
| `label` | string, bắt buộc với mọi loại trừ `section` | Tiêu đề của group trong tài liệu và trong studio | Generator, studio |
| `n` | số nguyên, bắt buộc với `section`, duy nhất | Số thứ tự của phần như người xem thấy | Generator, overlay, studio |
| `name` | string, bắt buộc với `section` | Tên của phần như người xem thấy | Generator, overlay, studio |
| `shape` | string | Group được kể như thế nào: mạch kể của nó và những gì nhạc quyết định | Generator, builder |
| `reveal` | number, bar của nhạc, chỉ cho `section` | Bar mà tên phần được hiện lần đầu. Trước đó bộ đếm hiện `???`. Nếu không có, tên hiện từ bar đầu tiên của phần. Nó phải nằm trong các bar của phần | Generator, overlay |

Một bộ phim có thể thêm các trường riêng cho builder của mình. Phim tham chiếu đã cho mỗi phần một `idiom`, loại bản in cũ mà nó mượn phong cách, và cho mỗi mục copy một `signalThing`, vật trong hình mang màu dành riêng. Generator không kiểm tra cũng không in các trường mà nó không biết, nên chúng không xuất hiện trong tài liệu: hãy dặn builder đọc chúng trong file dữ liệu.

### Shot

| Trường | Kiểu | Ý nghĩa | Được đọc bởi |
|---|---|---|---|
| `id` | string, bắt buộc, duy nhất, chữ thường | Khóa của timeline và tên của file scene. Xem mục 6 | Generator, app, card, overlay, studio |
| `group` | string, bắt buộc | Id của group mà shot thuộc về | Generator, overlay, studio |
| `bar` | number, tính bằng bar, bắt buộc | Nơi shot bắt đầu | Generator, overlay, card |
| `bars` | number, tính bằng bar, bắt buộc, lớn hơn 0 | Shot kéo dài bao lâu | Generator, overlay, card |
| `tone` | `dark` hoặc `light`, bắt buộc | Nền mà shot đứng trên | Generator, card, app (màu chữ của transition `through`) |
| `title` | string, bắt buộc | Tên ngắn của shot cho con người | Generator, card, studio |
| `in` | object | Transition dẫn vào shot. Shot đầu tiên không có, mọi shot khác đều có một | Generator, app, card |
| `see` | string, bắt buộc | Những gì có trên màn hình | Generator, card |
| `move` | string, bắt buộc | Hình chuyển động theo nhạc như thế nào | Generator, card |
| `camera` | string, bắt buộc | Camera làm gì | Generator (kiểm tra và ghi vào tài liệu), card |
| `look` | string, bắt buộc | Đó là loại hình ảnh gì | Generator, card |
| `repeat` | `true`, tùy chọn | Shot cố ý lặp lại chuyển động camera hoặc transition của shot trước; tắt hai cảnh báo cho cặp này | Generator |

### Transition (`in` của một shot)

| Trường | Kiểu | Ý nghĩa | Được đọc bởi |
|---|---|---|---|
| `kind` | string, bắt buộc | Một khóa của `transitions` | Generator, app, card |
| `lead` | number, tính bằng beat, 0 trở lên, bắt buộc | Số beat lấy từ cuối shot trước | Generator, app |
| `tail` | number, tính bằng beat, 0 trở lên, bắt buộc | Số beat lấy từ đầu shot này | Generator, app |
| `focus` | `[x, y]`, pixel của frame gốc (master frame), y hướng xuống; chuyển sang định dạng khác theo tỉ lệ | Điểm mà transition xoay quanh. Mặc định: giữa sân khấu | App |
| `dir` | `[x, y]`, vector đơn vị, y hướng xuống | Hướng di chuyển. Mặc định: `[1, 0]` | App |
| `text` | string | Cho `through`: các chữ cái đứng trước camera | App |
| `size` | number, px | Cho `through`: kích thước của các chữ đó khi chúng mới xuất hiện | App |
| `note` | string | Điều mà một transition trong-thế-giới-hình (in-world) đòi hỏi ở builder | Generator, builder |

### Caption

| Trường | Kiểu | Ý nghĩa | Được đọc bởi |
|---|---|---|---|
| `group` | string, bắt buộc | Id của một group loại `section` | Generator, overlay |
| `kind` | string, bắt buộc | Câu nào của phần: một khóa của `lines` trong mục copy của phần đó. Các loại là của riêng phim; phim ví dụ của starter dùng `hook`, `idea` và `use`, phim tham chiếu dùng `problem`, `metaphor` và `when` | Generator, overlay, builder |
| `bar` | number, tính bằng bar, bắt buộc | Khi nào câu bắt đầu | Generator, overlay, builder |
| `bars` | number, tính bằng bar, bắt buộc | Câu ở lại bao lâu | Generator, overlay, builder |
| `how` | `plate`, `shot` hoặc `none`, bắt buộc | Cách câu đến với người xem. Xem mục 10 | Generator, overlay |
| `place` | `top`, `middle` hoặc `bottom` | Vị trí của plate. Bắt buộc với plate | Generator, overlay |
| `why` | string | Lý do chọn `how` và `place` | Generator, chủ phim, builder |

### File copy

| Trường | Kiểu | Ý nghĩa | Được đọc bởi |
|---|---|---|---|
| `comment` | string | File này là gì, và chủ phim đã duyệt nó khi nào | Chỉ con người |
| `labels` | object, loại caption tới string | Nhãn nhỏ trên plate của loại đó. Loại nào không có mục thì không có nhãn | Overlay |
| `accents` | object, loại caption tới khóa palette | Màu của thanh bên cạnh plate của loại đó. Mặc định: `signal` | Overlay |
| `title` | object, khóa tới mảng các dòng (hoặc một string) | Chữ của thẻ tiêu đề. Các khóa là của riêng phim | Generator (in ra trong tài liệu), builder của shot tiêu đề qua `COPY` trong `src/film.ts` |
| `closing` | object, khóa tới mảng các dòng (hoặc một string) | Chữ của thẻ kết. Các khóa là của riêng phim | Generator (in ra trong tài liệu), builder của shot kết qua `COPY` |
| `sections` | array, bắt buộc | Một mục cho mỗi group loại `section` có caption | Generator, overlay, builder |
| `sections[].group` | string, bắt buộc | Id của group. Generator và app đều nối (join) theo nó | Generator, overlay, builder |
| `sections[].n`, `.name` | số nguyên, string, bắt buộc | Phải bằng `n` và `name` của group | Generator |
| `sections[].lines` | object, loại caption tới mảng string, bắt buộc | Một câu cho mỗi loại caption, một string cho mỗi dòng trên màn hình | Generator, overlay, builder qua `captionFor` và `sectionOf` |

## 3. Một ví dụ tối giản

Ba shot của một bộ phim bịa ra về việc giữ cho một cây cảnh trong nhà sống. Cả hai file đều qua được generator của starter mà không cần sửa: đặt chúng thay cho `shots.json` và `copy.json` của một bản starter mới rồi chạy.

```json
{
  "comment": "Shot list of a film about keeping a houseplant alive. Bars are bars of the music, counted from zero. `in` is the transition that leads into a shot; lead and tail are in beats.",
  "transitions": {
    "cut": {"label": "Straight cut", "what": "Nothing is added."},
    "whip": {"label": "Whip", "what": "The old shot smears in one direction and the new one comes out of the smear."},
    "zoom-in": {"label": "Into a detail", "what": "IN-WORLD. The next shot is held in a detail of this one. The camera goes into it."}
  },
  "groups": [
    {"id": "open", "kind": "title", "label": "Title"},
    {"id": "water", "kind": "section", "n": 1, "name": "Watering", "reveal": 4,
      "shape": "Problem first, in the bars without drums. The name arrives with the answer, on the first kick."}
  ],
  "shots": [
    {"id": "open-windowsill", "group": "open", "bar": 0, "bars": 2, "tone": "dark", "title": "A plant on the sill",
      "see": "A windowsill at night, one pot, one drooping plant. The name of the film stands behind the pot in type as tall as the frame, so the leaves overlap the letters.",
      "move": "First bar: the pot alone. Second bar: one word of the name on each beat.",
      "camera": "Locked off, the frame gives a little on each word",
      "look": "Full-frame type behind a drawn object"},
    {"id": "water-drowned-roots", "group": "water", "bar": 2, "bars": 2, "tone": "light", "title": "Too much water",
      "in": {"kind": "zoom-in", "lead": 1, "tail": 0, "focus": [540, 1300], "note": "The camera goes into the soil of the pot on the sill. The next shot is inside that soil."},
      "see": "The pot cut in half, seen from the side. Water is poured in four times and stands at the bottom. The roots turn from white to brown, from the tips up.",
      "move": "One pour on each beat of the first bar. The roots darken through the second bar.",
      "camera": "Sinks from the rim of the pot to its bottom",
      "look": "Cross-section in flat colour"},
    {"id": "water-finger-test", "group": "water", "bar": 4, "bars": 4, "tone": "light", "title": "Two knuckles deep",
      "in": {"kind": "whip", "lead": 0.25, "tail": 0.25, "dir": [0, -1]},
      "see": "A finger goes into the soil up to the second knuckle and comes out dry. Only then the watering can tips. A paper label stuck in the pot carries the sentence.",
      "move": "Finger in on beat one, out on beat three. The can tips on the first beat of the third bar.",
      "camera": "Pushes in slowly, then punches in once when the can tips",
      "look": "Close view, paper label with printed type"}
  ],
  "captions": [
    {"group": "water", "kind": "problem", "bar": 2, "bars": 2, "how": "plate", "place": "top", "why": "The roots fill the lower half of the frame."},
    {"group": "water", "kind": "metaphor", "bar": 4.25, "bars": 1.75, "how": "shot", "why": "The sentence is printed on the label in the pot. It starts one beat late, after the whip has settled."},
    {"group": "water", "kind": "when", "bar": 6, "bars": 2, "how": "none", "why": "The can tips only after the finger comes out dry: the picture says it."}
  ]
}
```

```json
{
  "comment": "Every sentence the film shows, already broken into lines. Approved by the owner.",
  "labels": {"problem": "WITHOUT IT", "when": "DO THIS WHEN"},
  "title": {"name": ["Keep it", "alive"], "line": ["three habits", "for one plant"]},
  "closing": {"line": ["Look first,", "then water."]},
  "sections": [
    {"n": 1, "group": "water", "name": "Watering",
      "lines": {
        "problem": ["Water by the calendar", "and the roots drown."],
        "metaphor": ["Soil is a sponge:", "feel it before you fill it."],
        "when": ["Water when two knuckles", "of soil are dry."]
      }}
  ]
}
```

Với beat grid của starter (120 BPM), lần chạy in ra `3 shots, bars 0..8, 16.00s`. Các loại transition là ba trong số các loại trong `src/engine/transition.ts`; từ điển chỉ liệt kê những loại mà phim dùng hoặc có thể dùng. Một recap (phần tóm tắt) và một thẻ kết được viết giống như tiêu đề: một group loại `recap` hoặc `end` có `label`, cùng các shot của nó. Các loại caption `problem`, `metaphor` và `when` là lựa chọn của phim này: tên nào cũng được, miễn là `kind` của mỗi caption là một khóa của `lines` trong mục copy của phần đó.

## 4. Các bước kiểm tra

Generator đọc cả hai file và beat grid, kiểm tra mọi thứ, và chỉ ghi khi mọi bước kiểm tra đều đạt. Một lần chạy thất bại in ra một dòng cho mỗi lỗi, dạng `error: <message>`, rồi `<n> fault(s); nothing was written.`, và thoát với mã 1. Không file sinh ra nào bị động tới, nên các file không bao giờ mâu thuẫn nhau sau một lần chạy thất bại.

Các bước kiểm tra chạy theo hai vòng. Vòng đầu kiểm tra mọi trường đều có mặt và đúng kiểu; nếu có cái nào trượt, lần chạy dừng ở đó và liệt kê các lỗi đó. Vòng thứ hai kiểm tra các trường khớp với nhau thế nào, và liệt kê tất cả lỗi của nó cùng lúc. Sửa dữ liệu rồi chạy lại.

### Vòng đầu: file và trường

| Kiểm tra | Thông báo khi thất bại |
|---|---|
| File dữ liệu tồn tại và là JSON hợp lệ | `the shot list not found: <path>`, `<path> is not valid JSON: line <l>, column <c>: <why>` (tương tự với file copy, beat grid và `data/audio.json`) |
| Danh sách shot có `transitions` (một object), `groups`, `shots` và `captions` (các list) | ``shots.json: `<key>` is missing or is not a list`` (hoặc `an object`) |
| File copy có một list `sections` | ``copy.json: `sections` is missing or is not a list`` |
| Beat grid có ít nhất hai beat, tất cả đều là số | ``<grid file>: `beats` must be a list of at least two times in seconds`` |
| `data/audio.json` có `duration` | ``data/audio.json: `duration` is missing`` |
| Group có `id` kiểu string và `kind` hợp lệ | ``group <id>: needs a string `id` ``, ``group <id>: `kind` must be one of title, section, recap, end`` |
| `section` có `n` và `name`, và `reveal` là số | ``group <id>: a section needs a whole number `n` and a `name` ``, ``group <id>: `reveal` must be a bar number`` |
| Mọi group khác có `label` | ``group <id>: a <kind> group needs a `label` `` |
| Shot có đủ mọi trường mô tả, không rỗng | ``shot <id>: `<field>` is missing or empty`` cho `id`, `group`, `title`, `see`, `move`, `camera`, `look` |
| Shot có `bar` và `bars`, và `bars` lớn hơn 0 | ``shot <id>: `<bar or bars>` must be a number of bars``, ``shot <id>: `bars` must be more than 0`` |
| `tone` là `dark` hoặc `light` | ``shot <id>: `tone` must be dark or light`` |
| Id viết thường | `shot <id>: ids are lower case (the id is the name of the scene file)` |
| `in` là object có `lead` và `tail` từ 0 trở lên | ``shot <id>: `in` must be an object``, ``shot <id>: `in.<lead or tail>` must be a number of beats, 0 or more`` |
| Caption có `group`, `kind`, `bar`, `bars` | ``caption <group>/<kind>: `<field>` is missing``, ``caption <group>/<kind>: `<bar or bars>` must be a number of bars`` |
| `how` là `plate`, `shot` hoặc `none` | ``caption <group>/<kind>: `how` must be one of plate, shot, none`` |
| Plate có `place` | `caption <group>/<kind>: a plate needs a place: top, middle, bottom` |
| Mục copy có `group`, `n`, `name` và `lines` đúng dạng | ``copy.json sections #<i>: needs a `group` ``, ``copy.json section <group>: needs `n` and `name`, equal to those of its group``, ``copy.json section <group>: `lines` must map each caption kind to a list of lines`` |

### Vòng thứ hai: dữ liệu khớp với nhau thế nào

| Kiểm tra | Vì sao có nó | Thông báo khi thất bại |
|---|---|---|
| Không có hai group trùng id, không có hai shot trùng id | Id là một khóa, và id của shot là tên file | `two groups share an id`, `two shots share the id <id>` |
| Có ít nhất một shot | Không có gì để phát | `shots.json has no shots` |
| Mọi loại trong từ điển đều là loại engine có thể chạy | Một loại engine không biết sẽ lỗi trong app, không phải trong generator | ``transition kind `<kind>` is in shots.json but the engine cannot play it (src/engine/transition.ts)`` |
| Hai shot liền nhau không có cùng nội dung `camera`, trừ khi shot sau ghi `"repeat": true` | Một chuyển động lặp lại theo thói quen sẽ không ai để ý, và một cột không ai kiểm tra sẽ xuống cấp dần. Đây là cảnh báo, không phải lỗi: một sự lặp lại mang ý đồ (một vòng lặp, một nhịp điệu của các cú zoom đều nhau, một chuyển động kéo qua nhiều shot) thì được đánh dấu và giữ lại | Cảnh báo: `shots <a> and <b> make the same camera move` |
| Shot đầu tiên không có `in` | Không có shot nào trước nó để lấy beat | `the first shot has nothing to lead in from` |
| Mọi shot khác có một `in` mà `kind` là một khóa của `transitions` | Mỗi cú cắt là một quyết định. Một cú cắt thường cũng được ghi lại như vậy | ``shot <id>: `in` must name one of <kinds>`` |
| Hai shot liền nhau không vào bằng cùng một loại, trừ `cut`, `travel` và `match`, và trừ khi shot sau ghi `"repeat": true` | Một hiệu ứng lặp lại theo thói quen sẽ bị đọc ra là thói quen. Ba ngoại lệ là những cú cắt thường đối với engine. Đây là cảnh báo, không phải lỗi: một bộ phim xây trên một thủ pháp lặp lại (zoom vào từng vật lồng nhau) thì đánh dấu các lần lặp | Cảnh báo: `shots <a> and <b> come in by the same transition` |
| Lead của một transition và tail của transition trước nó vừa trong shot nằm giữa chúng | Nếu không, shot đó không bao giờ được thấy đúng như builder đã dựng | `shot <id>: the lead of its transition runs into the tail of the one before` |
| Tail của một transition không dài hơn shot của nó | Như trên | `shot <id>: the tail of its transition is longer than the shot` |
| Mỗi shot bắt đầu ở đúng bar mà shot trước kết thúc | Không hở và không chồng: các shot phủ kín nhạc | `shot <id> starts at bar <bar>, the one before ends at bar <bar>` |
| `group` của shot tồn tại | Tài liệu và overlay tra cứu group | `shot <id> belongs to unknown group <group>` |
| Các shot của một group đi liền nhau | Các bar của một group được lấy từ shot đầu và shot cuối của nó | `the shots of group <group> are not together: shot <id> comes after shots of another group` |
| Mọi group đều có shot | Một group không có bar thì không đặt được | `group <id> has no shot` |
| `reveal` nằm trong các bar của phần đó | Một cái tên hiện trước hoặc sau phần của nó sẽ không bao giờ được thấy | ``group <id>: `reveal` <bar> lies outside its bars <a>..<b>`` |
| Một mục copy thuộc về một group `section`, và chỉ một lần | Phép nối theo `group` phải là một-một | `copy.json has two entries for group <group>`, `copy.json has an entry for <group>, which is not a section group in shots.json` |
| `n` và `name` của mục copy bằng của group | Tài liệu, bộ đếm và copy phải hiện cùng một số và một tên | ``copy.json section <group>: `n` and `name` (<n>, <name>) differ from its group (<n>, <name>)`` |
| Không có hai phần trùng số | Bộ đếm sẽ hiện một số hai lần | `two sections have the number <n>` |
| Một phần có caption thì có mục copy | Các caption của nó không có chữ | `section <id> has captions but no entry in copy.json` |
| Caption chỉ tới một group đã biết loại `section` | Chỉ các phần mới mang caption | `caption <group>/<kind>: unknown group <group>`, `caption <group>/<kind>: captions belong to numbered sections; <group> is a <kind> group` |
| Caption nằm trong các bar của phần của nó | Một câu không được tràn sang phần bên cạnh | `caption <group>/<kind> runs outside bars <a>..<b>` |
| Mục copy có câu thuộc loại của caption | Caption không có chữ thì không hiện gì | ``caption <group>/<kind>: copy.json has no sentence `<kind>` for <group>`` |
| Các caption của một phần không chồng nhau | Overlay hiện mỗi lần một caption: cái đầu tiên khớp | `captions <group>/<a> and <group>/<b> overlap: the overlay shows one caption at a time` |

Bước kiểm tra các loại với engine đọc list `export const TRANSITION_KINDS = [...]` trong `src/engine/transition.ts`. Nếu file không có hoặc không tìm thấy list đó, bước kiểm tra này bị bỏ qua mà không báo gì.

Hai trường hợp đưa ra cảnh báo nhưng không dừng lần chạy: các shot chạy quá cuối audio (`the shot list runs to <t> s, past the end of the audio at <d> s; the last shot is cut there`), và các shot chạy quá beat cuối của grid (`the shot list runs past the last beat of the grid (bar <b>); times after it are extrapolated`).

### Những bước kiểm tra nên thêm

**Không cái nào trong số này có trong generator của starter.** Mỗi cái là một quy tắc từng được giữ bằng tay.

| Kiểm tra nên thêm | Vì sao |
|---|---|
| Thời gian đọc: độ dài một câu tính bằng từ hoặc ký tự so với thời gian nó ở trên màn hình tính bằng giây | Một câu không đọc kịp trong thời gian của nó thì coi như không được truyền tải. Thống nhất giới hạn với chủ phim trong animatic |
| Không caption nào bắt đầu trong tail của một transition dẫn vào drop | Vài beat đầu sau một drop nằm dưới một cú lóe sáng và một sóng xung kích |
| Ngân sách cho transition in-world: số lượng của chúng giữ dưới một con số đã thống nhất với chủ phim | Chúng là những hình mạnh nhất và tốn kém nhất, và mất sức nặng khi xuất hiện dày |
| Mọi transition in-world đều có `note` | Tài liệu liệt kê các transition in-world dựa vào sự có mặt của `note`. |
| Mỗi drop được vào bằng một loại khác nhau | Đoạn build (dồn nén) trước một drop là điểm nhấn chính, và một cái lặp lại sẽ bị đoán trước. Generator chỉ so sánh các shot liền kề |
| Transition `through` có `text` | Không có chữ thì transition không có gì để đi xuyên qua |
| Các khóa của `labels` và `accents` là các loại caption, và mỗi accent là một khóa palette | Một loại viết sai chính tả sẽ mất nhãn mà không báo gì |

Từ thực tế: plate dày chữ nhất được duyệt của phim tham chiếu mang khoảng năm âm tiết mỗi giây (19 âm tiết tiếng Việt trong hai bar, 3,7 giây). Một caption bắt đầu hai beat sau một drop, và `why` của nó ghi rõ điều đó. Một caption khác của cùng phim vẫn bắt đầu ngay trên cú cắt của một drop. Một quy tắc giữ bằng tay thì được giữ phần lớn thời gian.

## 5. Những gì được sinh ra

| Đầu ra | Đường dẫn | Nội dung | Được đọc bởi |
|---|---|---|---|
| Tài liệu storyboard | `STORYBOARD.md` | Xem bảng bên dưới | Chủ phim, builder |
| Ranh giới shot tính bằng bar | `data/film-sections.json` | Một `{name, bar, bars}` cho mỗi shot | Bước phân tích nhạc (`analysis/analyze-beat-grid.py --sections data/film-sections.json`), để một lần phân tích mới ghi ra đúng các ranh giới đó. App không đọc nó |
| Thời gian shot trong dữ liệu audio | khóa `sections` của `data/audio.json` | Một `{name, start, end}` cho mỗi shot, tính bằng giây | App: một mục timeline cho mỗi section |

Bar được đổi sang giây qua beat grid của dữ liệu audio, không bao giờ qua một con số tempo: beat bằng bar nhân bốn, đếm từ bar 0 như bên dưới, và một thời điểm nằm giữa hai beat thì được nội suy. Shot cuối giữ thời điểm kết thúc cũ nếu tên và điểm bắt đầu của nó không đổi; nếu không, nó kết thúc ở bar cuối của nó, hoặc ở chỗ audio kết thúc nếu chỗ đó đến trước. Timeline kéo giãn mục đầu và mục cuối để phủ kín toàn bộ track. Phần còn lại của dữ liệu audio được giữ nguyên. Mỗi file được ghi ra một file tạm rồi đổi tên vào đúng chỗ.

Bar 0 bắt đầu ở downbeat (phách mạnh) đầu tiên của grid (`downbeats[0]`), cùng bar 0 mà `analysis/analyze-beat-grid.py --sections`, `barAt` trong `src/engine/audio.ts` và `beat-cues.ts` đếm từ đó. Các beat trước nó là phần pickup (phách lấy đà). Một grid không có `downbeats` thì bắt đầu bar 0 ở beat đầu tiên. Shot đầu tiên vẫn phát từ thời điểm 0, và đồng hồ scene của nó giữ phần pickup ở beat 0 (`kit-frame.ts`).

Tài liệu có bốn phần. Các tiêu đề, đầu bảng và vài câu giải thích chúng được cố định trong generator; mọi thứ khác lấy từ dữ liệu.

| Phần của tài liệu | Lấy từ |
|---|---|
| Dòng tiêu đề: `Storyboard: <film>` | `title` trong `src/project-config.ts` |
| 1. Tổng quan: số bar, độ dài, thời điểm bắt đầu, số shot và cách kể của mỗi group; tổng số shot, bar và giây | `groups`, `shots`, beat grid |
| 2. Transition: mọi loại trong từ điển cùng số lần dùng; các transition có `note`, kèm bar và thời gian; các cú cắt vào drop, kèm lead và tail | `transitions`, `in`, và list `DROP_KINDS` trong `src/engine/transition.ts` |
| 3. Chữ trên màn hình: ba cách và tần suất dùng mỗi cách; mọi câu của mọi phần, một cột cho mỗi loại caption; chữ của thẻ tiêu đề và thẻ kết | `captions`, file copy |
| 4. Từng shot một: một tiêu đề cho mỗi group kèm `shape` và `reveal`, một bảng các shot của nó, và một bảng các caption kèm chữ | `groups`, `shots`, `captions`, file copy |

Tài liệu không chứa brief, không có danh sách chuyển động camera và không có kế hoạch giao hàng. Brief là một trang riêng (xem `interview.md`). Phim nào muốn thêm gì vào tài liệu thì thêm vào bản generator của riêng mình.

```sh
bun run shots
# with another beat grid: any JSON file with a "beats" list, and "downbeats" if bar 0 is not its first beat
bun run shots -- path/to/grid.json
```

`bun run shots` khởi động generator bằng Python 3 đầu tiên nó tìm thấy (`scripts/python.ts` thử `python3`, rồi `python`, rồi `py -3`, và bỏ qua stub của Windows Store); biến môi trường `PYTHON` chỉ định một cái khác. Không có bun thì chạy trực tiếp: `python3 scripts/build-shot-files.py`, hoặc `python` hay `py -3` trên Windows. Generator là Python 3 thuần không cần package, và tìm file dựa vào vị trí của chính nó, nên có thể chạy từ bất kỳ thư mục nào. Với beat grid khác, `duration` và thời gian shot cũ vẫn lấy từ `data/audio.json`, và đó là file nó ghi. Một lần chạy đạt in ra các cảnh báo (nếu có), rồi số shot, các bar chúng phủ và độ dài tính bằng giây, rồi một dòng cho mỗi file. Dữ liệu audio được báo là `unchanged` khi không có thời gian shot nào thay đổi. Khi thiếu `data/audio.json`, thông báo nêu lệnh tạo một click grid: `bun run make-grid -- --bpm 120 --bars 24`.

**Không bao giờ sửa file được sinh ra.** Lần chạy sau sẽ ghi đè nó. Muốn đổi một shot hay một caption, sửa dữ liệu. Muốn đổi phần chữ cố định của tài liệu, sửa generator.

## 6. Id của shot

| Sự thật | Hệ quả |
|---|---|
| Id là tên của section trong dữ liệu audio và là khóa của mục timeline | Đổi id là đổi bản dựng |
| Id là tên file scene: shot `a-b` được phát bởi `src/scenes/a-b.ts` | Shot nào có id mà không có file thì được phát bằng thẻ storyboard |
| Timeline chuyển tên về chữ thường trước khi tìm file, và generator từ chối id không viết thường | Viết id bằng chữ thường |
| Lệnh capture và báo cáo mang id của shot. Các file phần (part file) của builder mang id của section | Một id bị đổi tên để lại một vệt tên cũ |

- Khi một id đổi trong danh sách shot mà file vẫn giữ tên cũ, shot đã dựng sẽ quay về thành thẻ mà không báo lỗi. Bộ đếm shot đã dựng trong studio (`<n> of <m> shots built`) sẽ cho thấy điều đó.
- Khi thứ tự các phần thay đổi, một id có chứa số thứ tự của phần sẽ chỉ sai chỗ. Đổi tên nghĩa là đổi file, file phần, import và báo cáo.
- Chọn id từ chủ đề của phần và hình ảnh của shot, ví dụ `water-finger-test`. Không đặt số thứ tự của phần vào id. Số thứ tự của shot trong phần cũng lỗi thời theo cách tương tự khi một shot bị bỏ hoặc được thêm.
- Con số người xem thấy đến từ trường `n`, không bao giờ từ id.

Từ thực tế: chủ của phim tham chiếu đã chuyển phần đầu xuống cuối và phần cuối lên đầu sau khi mọi shot đã được dựng. Id và tên file được giữ nguyên, nên các file tên `p8-*` giờ phát phần 01 và các file tên `p1-*` phát phần 08. Một shot bị bỏ để lại một khoảng trống: `p1-1` được theo sau bởi `p1-3`. Bộ phim phải có một đoạn cảnh báo cho người đọc kế tiếp.

## 7. Viết một shot

Bốn trường mô tả hình ảnh. Builder phải dựng được từ chúng, và chủ phim phải hình dung được shot từ chúng.

| Trường | Nói gì | Yếu | Mạnh |
|---|---|---|---|
| `see` | Các vật trên màn hình, trạng thái lúc đầu và lúc cuối, và mọi chữ xuất hiện, đúng từng ký tự | "An animation that shows the problem of too much water." ("Một animation cho thấy vấn đề tưới quá nhiều nước.") | "The pot cut in half, seen from the side. Water is poured in four times and stands at the bottom. The roots turn from white to brown, from the tips up." ("Chậu cây bị cắt đôi, nhìn từ bên hông. Nước được đổ vào bốn lần và đọng ở đáy. Rễ chuyển từ trắng sang nâu, từ chóp lên.") |
| `move` | Sự kiện nào rơi vào beat hay bar nào của shot, và trạng thái của nhạc | "Synchronised with the beat." ("Đồng bộ với nhịp.") | "One pour on each beat of the first bar. The roots darken through the second bar." ("Mỗi beat của bar đầu một lần đổ. Rễ sẫm dần suốt bar thứ hai.") |
| `camera` | Một chuyển động thuộc bộ chuyển động của phim, kèm điểm bắt đầu và kết thúc | "Dynamic camera." ("Camera năng động.") | "Sinks from the rim of the pot to its bottom" ("Hạ từ miệng chậu xuống đáy") |
| `look` | Loại hình ảnh | "Modern and clean." ("Hiện đại và gọn gàng.") | "Cross-section in flat colour" ("Mặt cắt ngang tô màu phẳng") |

- Gọi tên sự vật, không gọi tên phẩm chất. "Đẹp", "năng động" và "cuốn hút" chẳng cho builder thứ gì để vẽ.
- Đếm bằng đơn vị của nhạc. Một shot hai bar có tám beat, và `move` nói mỗi beat dùng để làm gì.
- Khi có một khái niệm lân cận gần giống, hãy viết vào `see` những gì shot không được cho thấy.
- Mô tả là ý đồ. Builder nào tìm ra cách tốt hơn để thể hiện cùng một điều thì cứ dùng và báo lại.
- Bước kiểm tra camera so sánh văn bản. Hai cách diễn đạt của cùng một chuyển động vẫn qua được, nên lead cũng phải đọc cột này.

Từ thực tế: sau khi chủ phim phát hiện những shot của phim tham chiếu dạy sai khái niệm, hai mô tả được thêm một câu kết dạng "Not one press that reports to many places" ("Không phải một máy ép báo về nhiều nơi"). Builder đã dựng đúng những gì storyboard yêu cầu, và dựng tốt. Lỗi nằm ở storyboard.

## 8. Định hình một phần

Một mạch kể khả dĩ cho một phần giải thích một ý tưởng: vấn đề trước, rồi ý tưởng, rồi nơi nó được dùng. Cái đau của vấn đề là thứ khiến ý tưởng đáng nhớ. Hãy dùng mạch này như nội dung của mỗi phần chứ không phải hình thức của nó: khi mọi phần đều chạy qua cùng các bước, người xem sẽ đoán được phần còn lại sau phần thứ hai.

| Cách phá khuôn | Nghĩa là gì | Hiện ra ở đâu trong dữ liệu |
|---|---|---|
| Độ dài không đều | Phần ngắn nhất có thể chỉ dài bằng nửa phần dài nhất | Tổng `bars` của mỗi phần |
| Đổi thứ tự kể | Mở đầu bằng câu trả lời rồi tua lại về vấn đề. Mở đầu bằng một câu đùa | Thứ tự các shot, `shape` |
| Dời khoảnh khắc then chốt | Tên của phần đến ở đầu, ở giữa, hoặc như dòng cuối cùng | `reveal` của group |
| Để nhạc quyết định | Đoạn build mang căng thẳng, drop mang câu trả lời, một bar không có trống mang thứ cần đọc | `bar` của shot then chốt bằng bar của drop |
| Đổi điểm nhìn | Ngôi thứ nhất, từ trên xuống, cận cảnh | `camera`, `look` |

Mỗi phần vẫn truyền tải đủ mọi ý của nó. Giữ thật ít thứ cố định cho cả phim, và nêu tên chúng trong tài liệu.

Từ thực tế: bản nháp đầu của phim tham chiếu kể mọi phần theo cùng bảy bước, mỗi phần mười hai bar. Chủ phim yêu cầu một cách kể không cứng nhắc. Trong bản nháp thứ hai, các phần dài từ 8 đến 14 bar, và tên phần đến sau khi phần bắt đầu từ 0 đến 7 bar.

### Nhân vật trong một phần

Trong phim có nhân vật, hãy viết vào `shape` của mỗi group vị trí đứng và hướng nhìn của từng nhân vật, và vào `see` của mỗi shot nhịp truyện (story beat), cảm xúc của nhân vật, và cỡ cảnh mà khuôn mặt nó cần để đọc được. Giữ đúng phía: một nhân vật đứng bên trái nhìn sang phải thì ở nguyên đó qua các cú cắt của một phần, trừ khi có shot cho thấy nó băng qua. Phần còn lại nằm trong `characters-and-story.md`.

### Giữ các khái niệm lân cận tách bạch

Một bộ phim giải thích nhiều khái niệm liên quan có thể cho thấy một hình đẹp nhưng dạy sai khái niệm. Việc duyệt hình không phát hiện được điều này. Hãy kiểm tra trong storyboard, trước khi dựng.

| Việc | Cách làm |
|---|---|
| Viết ranh giới cho mỗi khái niệm | Một dòng về những gì nó phải cho thấy, một dòng về những gì nó không bao giờ được cho thấy. Dòng thứ hai đến từ các khái niệm lân cận |
| Đặt từng shot cạnh các ranh giới | Che tên đi: người xem có thể gọi shot bằng tên của một khái niệm khác không? |
| Không dùng chung ví dụ | Hai khái niệm không dùng cùng một ví dụ, cùng một đạo cụ hay cùng một loại màn hình |
| Kiểm tra cả câu chữ | Từ khóa của khái niệm này không xuất hiện trong câu của khái niệm khác |
| Kiểm tra nội dung trước khi trau chuốt | Công sức bỏ vào một shot mà nội dung phải thay đổi là công sức mất trắng |

## 9. Định hình bộ phim

| Phần | Loại | Nhiệm vụ | Dài bao lâu |
|---|---|---|---|
| Tiêu đề | `title` | Nêu tên phim và lời hứa của nó | Vài bar, tới ranh giới đầu tiên mà nhạc đưa ra |
| Các phần | `section` | Mỗi phần một ý | Do các câu nhạc (phrase) quyết định, và cố ý không đều |
| Recap | `recap` | Mọi tên phần thêm một lần | Mỗi tên một beat là đủ |
| Thẻ kết | `end` | Một câu duy nhất để mang về | Tới cuối track. Có thể kết thúc ở một phần lẻ của bar |

- Các shot phủ kín nhạc từ bar 0 tới cuối track. Tổng độ dài là một giới hạn của brief.
- Thứ tự các phần là quyết định của chủ phim. Đề xuất một thứ tự kèm lý do, và hỏi.
- Một thay đổi thứ tự có cái giá của nó: `bar` của mọi shot bị dời, các bar của caption của nó, `reveal`, và `n` trong cả hai file. Một phần dời vào một chỗ có hình dạng nhạc khác thì phải viết lại và dựng lại.
- Giữ chi phí thấp bằng cách hoán đổi những chỗ có cùng hình dạng nhạc: cùng độ dài, và drop cùng các đoạn nghỉ ở cùng khoảng cách tính từ đầu. Một shot đã dựng đếm beat từ điểm bắt đầu của chính nó và phát y nguyên ở chỗ mới. Xem lại những shot đọc tiếng kick hay năng lượng của nhạc.
- Dựng tiêu đề và recap từ `n` của file copy, để chúng tự đi theo thứ tự mới.

Từ thực tế: trong phim tham chiếu, tiêu đề 3 bar, các phần 8, 10, 12 và 14 bar, recap 2 bar, thẻ kết 2,75 bar, khoảng 1,85 giây một bar. Khi hai phần đổi chỗ cho nhau, sáu phần ở giữa giữ nguyên bar và không cần dựng lại. Hai phần bị dời rơi vào những chỗ có hình dạng khác: một phần tăng từ bốn shot lên bảy, phần kia mất một shot.

### Một tác phẩm ngắn

Một tác phẩm thuộc short lane (luồng làm nhanh cho tác phẩm ngắn) giữ storyboard của nó trong cùng hai file, dưới dạng bảng beat (`short-pieces.md`, mục 5). Nó có một group loại `title` và có thể thêm một group loại `end`, không có group `section`, một list `captions` rỗng và một list `sections` rỗng trong file copy. Chữ của nó nằm dưới `title` và `closing` trong file copy. Các shot của nó là các trạng thái hoặc chuyển động của tác phẩm, mỗi cái một beat hoặc một bar; một cú quay liền mạch (continuous take) đi vào bằng `cut`. Generator kiểm tra và ghi nó như mọi storyboard khác: dạng này đã được chạy qua generator trong một bản starter.

## 10. Caption

Mỗi câu đến với người xem theo một trong ba cách. Kỹ thuật làm plate và chữ nằm trong `type-and-captions.md`.

| `how` | Ai đặt chữ | Chọn khi |
|---|---|---|
| `plate` | Overlay, trên một plate ở `place` | Hình cần một lời bình. Plate đứng ở chỗ hình chừa ra |
| `shot` | Builder, như một vật trong hình | Shot có một bề mặt mang chữ: một tấm vé, một tấm biển, một màn hình |
| `none` | Không ai | Khi che chữ đi, một người xem chẳng biết gì vẫn hiểu ý trong thời gian shot kéo dài |

- `place` đi theo hình. Một caption đứng cùng một chỗ ở mọi shot là lựa chọn nhàm chán.
- `bar` và `bars` nhận số lẻ. Một phần tư bar là một beat. Dùng chúng để bắt đầu một câu sau một tail, hoặc sau khi thứ chiếm chỗ của nó đã đi khỏi.
- `why` ghi lại lý do: hình nằm ở đâu, và vì sao câu bắt đầu lúc đó. Một lựa chọn không có lý do thì không duyệt được.
- Danh sách shot giữ đề xuất đầu tiên. Builder có thể đổi `how` và `place` cho một phần và báo lại, và lead cập nhật danh sách shot.
- Chữ là chữ đã được duyệt, đúng từng ký tự. Chúng chỉ nằm trong file copy. Builder nào có shot tự đặt chữ thì lấy chữ từ `captionFor` trong `src/film.ts`.
- Overlay chỉ vẽ caption lên các group loại `section`, và mỗi lần một caption.

## 11. Transition trong danh sách shot

Danh mục các loại và cách dựng chúng nằm trong `transitions.md`. Danh sách shot ghi lại loại nào dẫn vào shot nào.

- Một transition thuộc về shot mà nó dẫn vào. Shot đầu tiên không có, và mọi shot khác đều có một. Một cú cắt thường là `{"kind": "cut", "lead": 0, "tail": 0}`.
- `lead` và `tail` tính bằng beat. Lead được phát đè lên cuối shot trước, và những gì quan trọng trong shot đó phải xong trước lúc ấy. Tail được phát đè lên đầu shot này, và không chữ nào cần đọc được đứng bên dưới nó.
- `focus`, `dir`, `text` và `size` chỉ được ghi khi loại đó dùng chúng.
- `note` được viết cho transition mà một shot tham gia vào. Nó nói điều được yêu cầu ở builder của cả hai shot. Tài liệu liệt kê các transition này trong một bảng riêng, kèm bar và thời gian.
- Các loại engine chạy được là list `TRANSITION_KINDS` trong `src/engine/transition.ts`. Mọi khóa của từ điển `transitions` phải nằm trong đó, và generator kiểm tra điều này. Các loại dẫn vào drop là `DROP_KINDS` trong cùng file, và tài liệu dựa vào nó để liệt kê các cú cắt vào drop.
- Khi một trong hai shot vẫn còn là thẻ, engine phát một bản thay thế cho loại in-world, để animatic vẫn cho thấy ý đồ.

Từ thực tế: phim tham chiếu có 53 cú cắt. Sáu cái là transition in-world và năm cái dẫn vào drop. Sau khi chủ phim yêu cầu có transition in-world, lead bắt đầu biến nhiều cú cắt thành loại đó, và chủ phim đã sửa lại: chỉ vài cái, ở những khoảnh khắc quan trọng.

## 12. Animatic và cổng duyệt

Studio phát mọi shot của danh sách shot theo thứ tự, cùng với nhạc. Shot nào không có file scene thì được phát bằng thẻ storyboard.

| Thẻ hiển thị | Lấy từ |
|---|---|
| Id và các bar | `id`, `bar`, `bars` |
| Tiêu đề, khẽ nảy trên mỗi beat | `title` |
| Những gì trên màn hình, cách nó chuyển động, camera, look | `see`, `move`, `camera`, `look` |
| Tên của transition dẫn vào shot | `in.kind`, qua từ điển |
| Một ô vuông cho mỗi beat của shot, ô đang phát sáng lên | `bars` và beat grid |

Trên một thẻ, overlay hiện mọi caption, kể cả những caption có `how` là `shot` và `none`, được đánh dấu như vậy. Chủ phim có thể đọc mọi câu trước khi có bất kỳ hình nào.

Chủ phim đánh giá ba điều trong animatic mà tài liệu không cho thấy được: nhịp điệu của các cú cắt, độ dài của mỗi phần, và liệu các câu có đọc kịp trong thời gian của chúng không.

Cổng duyệt: chủ phim xem animatic, đọc tài liệu, và nói rằng nội dung và look đã chốt. Không shot nào được dựng trước lúc đó. Duyệt một mục lục không phải là cho phép dựng. Những việc không chứa nội dung và look có thể tiến hành: nhạc, beat grid, engine, studio. Tắt server của studio khi buổi xem kết thúc.

Từ thực tế: chủ phim duyệt một bảng các ý của phim tham chiếu, và lead liền chuyển sang palette, font và code dùng chung. Chủ phim dừng công việc lại, rồi thêm một yêu cầu làm thay đổi cấu trúc của mọi phần.

## 13. Thay đổi storyboard khi đã có shot

| Bước | Làm gì |
|---|---|
| 1 | Xem từng shot sẽ thay đổi, như hiện tại. Ghi lại những hình ảnh nó đang có |
| 2 | Đánh dấu "giữ" cạnh những gì chủ phim đã khen và những gì mang ý tưởng. Những gì bị bỏ khỏi một shot bị rút ngắn là quyết định của lead |
| 3 | Sửa danh sách shot hoặc file copy. Chạy generator |
| 4 | Báo cho từng builder: các id đã đổi, các bar mới, nhiệm vụ mới của shot, những hình cần giữ, các transition giờ chạm tới shot |
| 5 | Báo cho chủ phim những gì bị bỏ |
| 6 | Xem phần đã đổi trong studio, xuyên qua các cú cắt của nó |

- Đưa thư mục phim vào version control trước vòng sửa đầu tiên. Khi đó một hình bị mất vẫn tra lại được.
- Danh sách shot và file copy chỉ có một người viết, là lead. Builder nào thấy storyboard sai thì nói ra trong báo cáo.
- Dữ liệu audio có hai người viết. Bước phân tích nhạc ghi toàn bộ file, và generator thay thế thời gian shot trong đó. Chạy chúng lần lượt, không bao giờ cùng lúc, và chạy generator sau cùng.

Từ thực tế: một shot của phim tham chiếu được dời vào một drop và được giao mang tên của phần. Brief gửi builder mô tả nhiệm vụ mới mà không nhắc đến hình ảnh shot đã có. Builder thay nó đi, chủ phim lần xem đầu không nhận ra, và phải mất thêm hai vòng nữa. Bộ phim không có version control, nên hình cũ không tra lại được.

## 14. So sánh với các file trạng thái của HyperFrames

| Vai trò | Lối đi này | HyperFrames |
|---|---|---|
| Ý đồ đã xác nhận | Trang brief chủ phim đã xác nhận (`interview.md`). Tài liệu storyboard không lặp lại nó | `BRIEF.md` |
| Kế hoạch của phim | Danh sách shot dạng dữ liệu, tài liệu sinh ra từ nó | `STORYBOARD.md`, viết trực tiếp: frontmatter và một mục `## Frame N` cho mỗi frame |
| Trạng thái mỗi shot | Không lưu. Một shot là đã dựng khi tồn tại một file scene mang id của nó | Trạng thái trong `STORYBOARD.md`: `outline`, rồi `built`, rồi `animated` |
| Chữ | File copy | `SCRIPT.md` cho lời dẫn đã chốt, `caption_groups.json` |
| Quy tắc của look | Treatment và hướng dẫn dựng (authoring guide) | `frame.md` |
| Những gì chủ phim duyệt trước khi dựng | Animatic, cùng với nhạc, và tài liệu | `storyboard.html`, một tờ phác thảo tĩnh |
| Định thời | Beat grid và thời gian shot trong dữ liệu audio | `audio_meta.json`, `beats/` |
| Bộ phim | Một module scene cho mỗi id shot | `index.html` và `compositions/frames/NN-*.html` |
| Brief cho builder | Hướng dẫn dựng và brief của lead | `.hyperframes/frame-packets/` |

HyperFrames duyệt storyboard trước khi dựng khi brief ghi `storyboard: yes`. Ở lối đi này, cổng duyệt không phải là tùy chọn. HyperFrames đặt tên file frame theo số thứ tự, đúng thói quen mà mục 6 khuyên tránh. Cả hai lối đi tình cờ đều đặt tên tài liệu storyboard là `STORYBOARD.md`; ở đây nó được sinh ra và không bao giờ bị sửa tay. Cột bên phải lấy từ `hyperframes-facts.md`.

## 15. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Một shot đã dựng lại thành thẻ | Id của nó đổi trong danh sách shot còn file thì giữ tên | Đổi tên cả hai cùng lúc, hoặc giữ id |
| Tên file hiện sai số của phần | Id chứa số thứ tự, và thứ tự đã đổi | Id không chứa số thứ tự. Số trên màn hình lấy từ `n` |
| Lần chạy kết thúc bằng `nothing was written` | Một bước kiểm tra thất bại | Đọc mọi dòng `error:`. Sau khi vòng kiểm tra trường đạt, vòng thứ hai có thể liệt kê thêm lỗi |
| Một chỉnh sửa trong tài liệu biến mất | Tài liệu được sinh ra | Sửa dữ liệu, hoặc phần chữ cố định trong generator |
| Một trường thêm cho builder không có trong tài liệu | Generator chỉ in những trường nó biết | Chỉ builder tới file dữ liệu, hoặc in trường đó từ generator |
| Người xem đoán trước được phần kế tiếp | Một khuôn cho mọi phần | Mục 8 |
| Một shot đẹp lại dạy một khái niệm lân cận | Storyboard đã yêu cầu nó | Ranh giới cho mỗi khái niệm, kiểm tra trước khi dựng |
| Một câu không đọc kịp | Nó bắt đầu dưới cú va của một drop, hoặc quá dài so với số bar của nó | Bắt đầu nó sau tail. Đánh giá thời gian trong animatic |
| Một plate không có nhãn, hoặc sai màu | Loại của nó bị thiếu hoặc viết sai trong `labels` hay `accents` | Dùng các loại caption của `lines` làm khóa |
| Hai shot liền nhau chuyển động giống nhau mà bước kiểm tra vẫn qua | Bước kiểm tra so sánh văn bản | Lead đọc cột camera |
| Một loại qua được generator nhưng lỗi trong app | Generator không đọc được `TRANSITION_KINDS` trong `src/engine/transition.ts` và đã bỏ qua bước kiểm tra | Giữ list ở dạng đó: `export const TRANSITION_KINDS = [...]` với các tên trong dấu nháy |
| Chủ phim dừng công việc lại | Việc dựng đã bắt đầu sau khi một mục lục được duyệt | Chờ ở cổng duyệt cho tới khi có lệnh đi rõ ràng |
| Một hình chủ phim thích đã biến mất | Brief sửa lại không nhắc tới nó | Liệt kê các hình của shot, đánh dấu những gì cần giữ |
| Mọi cú cắt đều thành transition in-world | Lead đã thay thế trong khi chủ phim yêu cầu thêm | Hỏi: thêm, hay thay? Giữ một ngân sách |
| Thời gian shot sai sau một lần phân tích nhạc mới | Bước phân tích đã ghi lại dữ liệu audio sau khi generator chạy | Chạy generator sau cùng |
