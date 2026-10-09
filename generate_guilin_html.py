# -*- coding: utf-8 -*-
import hashlib
import re

# 读取基准骨架的 style
skeleton_path = "C:/Users/byhoo/.gemini/config/skills/jianhao-travel-planner/assets/路书_基准骨架.html"
with open(skeleton_path, "r", encoding="utf-8") as f:
    skel_content = f.read()

style_match = re.search(r"<style[^>]*>(.*?)</style>", skel_content, re.S)
assert style_match, "Style not found in skeleton"
style_text = style_match.group(1)
style_md5 = hashlib.md5(style_text.encode("utf-8")).hexdigest()[:10]
print("Baseline Style MD5:", style_md5)

# 生成紧凑优雅的 SVG Data URI 示意图函数
def make_svg_data_uri(title, subtitle, bg_color="#2F5D43", accent_color="#E6EEE8"):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="g_{title[:4]}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_color}" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="{bg_color}" stop-opacity="0.98"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="14" fill="url(#g_{title[:4]})"/>
  <path d="M 0 320 Q 150 260 300 310 T 600 290 L 600 400 L 0 400 Z" fill="#ffffff" fill-opacity="0.12"/>
  <path d="M 80 340 L 140 220 L 200 340 Z" fill="#ffffff" fill-opacity="0.25"/>
  <path d="M 160 340 L 240 180 L 320 340 Z" fill="#ffffff" fill-opacity="0.2"/>
  <path d="M 380 340 L 460 210 L 540 340 Z" fill="#ffffff" fill-opacity="0.22"/>
  <circle cx="480" cy="90" r="36" fill="#F3EEDF" fill-opacity="0.3"/>
  <text x="40" y="70" font-family="-apple-system,BlinkMacSystemFont,PingFang SC,sans-serif" font-size="28" font-weight="bold" fill="#ffffff" letter-spacing="1">{title}</text>
  <text x="40" y="105" font-family="-apple-system,BlinkMacSystemFont,PingFang SC,sans-serif" font-size="16" fill="{accent_color}" letter-spacing="0.5">{subtitle}</text>
  <rect x="40" y="325" width="160" height="28" rx="6" fill="#ffffff" fill-opacity="0.2"/>
  <text x="50" y="344" font-family="-apple-system,BlinkMacSystemFont,PingFang SC,sans-serif" font-size="12" fill="#ffffff">桂林阳朔 · 亲子慢游</text>
</svg>"""
    import urllib.parse
    return "data:image/svg+xml;utf8," + urllib.parse.quote(svg)

# 12 张配图
img_d1_1 = make_svg_data_uri("象鼻山水月洞", "象山区 · 临江浅滩象鼻吸水", "#2F5D43", "#E6EEE8")
img_d1_2 = make_svg_data_uri("两江四湖日月双塔", "杉湖之畔 · 金银双塔初夜华灯", "#1E3A8A", "#DBEAFE")
img_d2_1 = make_svg_data_uri("芦笛岩钟乳石奇观", "地下魔宫 · 恒温20度水帘洞天", "#047857", "#D1FAE5")
img_d2_2 = make_svg_data_uri("东西巷与逍遥楼", "明清老街 · 临江城楼俯瞰两江", "#78350F", "#FEF3C7")
img_d3_1 = make_svg_data_uri("漓江三星级游船", "顺流而下 · 磨盘山至阳朔4小时画廊", "#0E7490", "#CFFAFE")
img_d3_2 = make_svg_data_uri("遇龙河山水民宿", "十里画廊 · 推窗揽峰林田园秘境", "#15803D", "#DCFCE7")
img_d4_1 = make_svg_data_uri("遇龙河平缓大筏", "万景码头 · 亲子老少皆宜平水悠漂", "#047857", "#D1FAE5")
img_d4_2 = make_svg_data_uri("十里画廊亲子骑行", "工农桥畔 · 凤尾竹与田园落日暮色", "#B45309", "#FEF3C7")
img_d5_1 = make_svg_data_uri("如意峰高空索道", "万峰丛林 · 无障碍高空玻璃天桥", "#4338CA", "#E0E7FF")
img_d5_2 = make_svg_data_uri("兴坪20元人民币背景", "元宝山下 · 实物纸币打卡漓江胜景", "#0F766E", "#CCFBF1")
img_d6_1 = make_svg_data_uri("遇龙河清晨薄雾", "山水晨曦 · 凤尾竹青与水墨长卷", "#374151", "#E5E7EB")
img_d6_2 = make_svg_data_uri("阳朔田园悠闲早茶", "慢调归途 · 满载山水回忆返程深圳", "#1F2937", "#F3F4F6")

html_text = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="generator" content="jianhao-travel-planner · 基准骨架 · 指纹 9c3c6249a4">
<title>桂林阳朔路书 · 亲子慢游版（两大一小）</title>
<script>document.documentElement.classList.add('js');</script>
<style>
{style_text}
</style>
</head>
<body>
<a class="skip" href="#main">跳到主要内容</a>
<div class="toolbar" role="group" aria-label="阅读工具">
  <button class="tbtn" id="fontDec" aria-label="字号调小">A−</button>
  <button class="tbtn" id="fontInc" aria-label="字号调大">A＋</button>
  <button class="tbtn" id="printBtn" aria-label="打印这份路书">🖨 打印</button>
</div>
<aside class="side">
  <div>
    <div class="logo">桂林阳朔<span>.</span></div>
    <div class="logo-sub">6天5晚 · 两大一小亲子版</div>
  </div>
  <nav aria-label="页面导航">
    <div class="nav-group">
      <div class="nav-label">行程</div>
      <a href="#overview">总览</a>
      <a href="#drive">路程</a>
      <a href="#day1">第 1 天 · 象山双塔</a>
      <a href="#day2">第 2 天 · 溶洞老街</a>
      <a href="#day3">第 3 天 · 漓江顺流</a>
      <a href="#day4">第 4 天 · 遇龙骑行</a>
      <a href="#day5">第 5 天 · 峰林纸币</a>
      <a href="#day6">第 6 天 · 晨雾归程</a>
      <a href="#boost">备选</a>
    </div>
    <div class="nav-group nav-group--chips">
      <div class="nav-label">备忘</div>
      <a href="#ticket">门票</a>
      <a href="#tips">提示</a>
      <a href="#stay">住宿</a>
      <a href="#cost">预算</a>
      <a href="#sos">应急</a>
      <a href="#eat">美食</a>
      <a href="#gift">特产</a>
    </div>
  </nav>
  <div class="side-foot">
    深圳北出发 · 11/17–11/22<br>
    两大一小家庭慢游<br>
    信息 2026-10-09 联网实查
  </div>
</aside>
<main id="main">
  <div class="wrap">

    <!-- 1. OVERVIEW -->
    <section id="overview">
      <div class="eyebrow">OVERVIEW · 亲子慢游总览</div>
      <h1>桂林阳朔山水路书</h1>
      <p class="lead">桂林山水甲天下，阳朔山水甲桂林。这是一份专为“两大一小”家庭定制的慢度假路书：拒绝清晨赶车、不搞特种兵暴走，主线全天 10:00 前后出发。大船顺流下漓江，竹筏与骑行轻踏遇龙河，兼顾大人度假放松与小朋友探奇。</p>
      <p class="lead"><strong>地理归属：</strong>广西壮族自治区桂林市（市区秀峰区/象山区 + 阳朔县漓江与遇龙河精华片区）。全程仅换 1 次酒店，动线顺滑。</p>
      
      <div class="warn-line">
        <b>⚠️ 出发前必办三件事（紧迫度排序）：</b><br>
        1. 提前 3~5 天在微信小程序【桂林漓江商城】预订 11/19 磨盘山至阳朔三星级游船（每日舱位固定，带娃锁连座）；<br>
        2. 关注微信公众号【遇龙河】，每晚 20:00 放次日票，两大一小认准【万景码头休闲大筏】（平稳无冲坝，1米以下全家可同乘）；<br>
        3. 微信小程序【象山景区】提前 1~3 天预约免费入园时段二维码。
      </div>

      <div class="weather">
        <div class="wday">
          <div class="d">11/17–11/18 · 桂林市区</div>
          <div class="w">晴到多云</div>
          <div class="t">16℃ ~ 24℃ · 舒适微风</div>
        </div>
        <div class="wday">
          <div class="d">11/19–11/20 · 漓江/阳朔</div>
          <div class="w">晴朗干爽</div>
          <div class="t">17℃ ~ 25℃ · 遇龙河晨温略低</div>
        </div>
        <div class="wday">
          <div class="d">11/21–11/22 · 兴坪/返程</div>
          <div class="w">多云转晴</div>
          <div class="t">18℃ ~ 24℃ · 适宜户外</div>
        </div>
      </div>
      <p style="font-size:0.75rem;color:var(--ink3);margin-top:6px;text-align:right">气象数据：当地历年同期气候与实时预报（出发前 3 天看当日预报终判）</p>

      <div class="card" id="prepCard" style="margin-top:20px">
        <h3>⏰ 出发前倒计时行动清单</h3>
        <ul class="check">
          <li><input type="checkbox" id="c1"><span class="ct"><b>T-7 天（11/10）</b>：12306 预订深圳北至桂林北高铁（G2904 或 G2908，09:30-10:30 档车次）及返程车票</span></li>
          <li><input type="checkbox" id="c2"><span class="ct"><b>T-5 天（11/12）</b>：提前办好【桂林漓江商城】11/19 磨盘山→阳朔三星级游船票（成人 ¥215，儿童优待票）</span></li>
          <li><input type="checkbox" id="c3"><span class="ct"><b>T-3 天（11/14）</b>：小程序【象山景区】预约 11/17 免费入园码；确认桂林大瀑布饭店与阳朔民宿亲子床围</span></li>
          <li><input type="checkbox" id="c4"><span class="ct"><b>T-1 天（11/16）</b>：打包儿童折叠伞车、防风薄外套、常用小药盒、手机防水袋，准备次日出发</span></li>
        </ul>
      </div>

      <div class="card" id="gear">
        <h3>🎒 亲子定制装备清单</h3>
        <p style="font-size:0.85rem;color:var(--ink2);margin-bottom:10px">针对 11 月华南初秋山水气候定制：白天温暖舒适，水面清晨及傍晚风凉。</p>
        <ul class="check">
          <li><input type="checkbox" id="g1"><span class="ct"><b>轻便折叠婴儿伞车</b>：象鼻山、东西巷、如意峰索道上站皆平缓，带娃推行省力</span></li>
          <li><input type="checkbox" id="g2"><span class="ct"><b>儿童防风卫衣/薄外套 2 件</b>：漓江游船顶层甲板、遇龙河早晚骑行防风保温</span></li>
          <li><input type="checkbox" id="g3"><span class="ct"><b>手机防水袋 2 个</b>：遇龙河竹筏与漓江船边拍照防跌落溅水</span></li>
          <li><input type="checkbox" id="g4"><span class="ct"><b>全家常备小药包</b>：蒙脱石散、小儿美林/退热贴、创可贴、碘伏棉棒、儿童防蚊滚珠</span></li>
          <li><input type="checkbox" id="g5"><span class="ct"><b>证件与电源</b>：全家身份证原件、儿童户口本/医保卡、大容量充电宝</span></li>
        </ul>
      </div>
    </section>

    <!-- 2. DRIVE -->
    <section id="drive">
      <div class="eyebrow">DRIVE & TRANSIT · 路程与交通</div>
      <h2>全程交通与接驳总表</h2>
      <p class="lead">全段严守“大船当大交通、市内正规网约车、田园亲子电动车”三大原则，避免家庭带着大包小包赶大巴。</p>

      <table class="tb">
        <thead>
          <tr><th>行程段落</th><th>交通方式</th><th>里程 / 预计耗时</th><th>核心衔接与注意事项</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><b>D1 深圳北 ➔ 桂林北</b></td>
            <td>直达高铁（G2904等）</td>
            <td>约 550 km · 3 小时 10 分</td>
            <td>车上安排儿童午餐与安静绘本；桂林北出站直接打车至酒店</td>
          </tr>
          <tr>
            <td><b>D1 桂林北 ➔ 市区酒店</b></td>
            <td>正规网约车（滴滴/高德）</td>
            <td>约 8 km · 25 分钟</td>
            <td>车费约 ¥30-40，平缓直达两江四湖湖畔酒店</td>
          </tr>
          <tr>
            <td><b>D2 市区 ➔ 芦笛岩</b></td>
            <td>正规网约车</td>
            <td>约 7 km · 18 分钟</td>
            <td>景区门口即下客区，推车平整入园，车费约 ¥20</td>
          </tr>
          <tr>
            <td><b>D3 市区 ➔ 磨盘山码头</b></td>
            <td>网约车 / 专车</td>
            <td>约 26 km · 40 分钟</td>
            <td>车费约 ¥65，09:00 前后出发，推车行李直接带上游船托运</td>
          </tr>
          <tr>
            <td><b>D3 磨盘山 ➔ 阳朔龙头山</b></td>
            <td>漓江三星级游船</td>
            <td>约 60 km · 4 小时航程</td>
            <td>平稳顺流而下，饱览九马画山与黄布倒影，全家不晕船</td>
          </tr>
          <tr>
            <td><b>D3 龙头山 ➔ 遇龙河民宿</b></td>
            <td>民宿专车接驳</td>
            <td>约 9 km · 20 分钟</td>
            <td>避开西街拥堵路段，直达遇龙河十里画廊田园腹地</td>
          </tr>
          <tr>
            <td><b>D4 遇龙河十里画廊</b></td>
            <td>国标亲子电动自行车</td>
            <td>全天慢骑约 12 km</td>
            <td>租带儿童安全护栏与头盔的电动车（¥40-50/天），随走随停</td>
          </tr>
          <tr>
            <td><b>D5 阳朔民宿 ➔ 如意峰/兴坪</b></td>
            <td>合规专车包车</td>
            <td>往返约 45 km · 全程分段</td>
            <td>包车约 ¥180-220/天，点对点接送，不用等车换乘</td>
          </tr>
          <tr>
            <td><b>D6 阳朔民宿 ➔ 阳朔高铁站</b></td>
            <td>专车接驳</td>
            <td>约 35 km · 45 分钟</td>
            <td>阳朔站位于兴坪镇，预留 45 分钟车程，搭乘高铁返深</td>
          </tr>
        </tbody>
      </table>

      <div class="note-row" style="margin-top:16px">
        <span class="ic">💳</span>
        <div><b>支付方式分层：</b>桂林及阳朔全程微信/支付宝极度便利；随身备 ¥200 纸币零钱，用于竹筏码头买鱼饲料、小吃摊与路边鲜榨甘蔗汁等零星找零场景。</div>
      </div>
      <div class="warn-line">
        <b>🚨 拥堵与时段预警：</b>阳朔西街核心路段在 17:30–21:00 极度拥堵且非机动车密集，本次动线住在遇龙河十里画廊内，完全避开西街晚高峰车辆堵塞。
      </div>
    </section>

    <!-- 3. DAY 1 -->
    <section id="day1">
      <div class="day">
        <div class="day-head">
          <div class="day-idx">DAY 01 · 2026-11-17</div>
          <h3>深圳抵桂 · 象鼻山与两江四湖夜漫步</h3>
          <span class="today-badge">· 今天</span>
        </div>

        <div class="note-row">
          <span class="ic">🧭</span>
          <div><b>今日速览：</b>上午=深圳北乘高铁直达桂林北；下午=入住酒店休整并探访象鼻山水月洞；傍晚=两江四湖杉湖畔看金银双塔夜景。</div>
        </div>

        <div class="photos">
          <figure>
            <img src="{img_d1_1}" alt="象鼻山水月洞" loading="lazy">
            <figcaption>象鼻山水月洞 · 临江浅滩巨石象鼻吸水（实景示意）</figcaption>
          </figure>
          <figure>
            <img src="{img_d1_2}" alt="两江四湖日月双塔" loading="lazy">
            <figcaption>两江四湖日月双塔 · 金银塔入夜倒影（实景示意）</figcaption>
          </figure>
        </div>

        <div class="slot">
          <div class="slot-time"><b>09:40</b></div>
          <div class="slot-body">
            <b>深圳北站乘高铁出发</b><br>
            推荐 G2904（09:48–12:58）或同档车次，耗时 3 小时 10 分钟。车上准备儿童涂色纸与轻食水果，列车平稳舒适。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>12:30</b></div>
          <div class="slot-body">
            <b>午餐 · 高铁轻食或下车第一碗米粉</b><br>
            出站打车 25 分钟抵达市区酒店办理入住。稍作休整后，在酒店步行 200 米处品尝【明桂米粉】卤菜粉（锅烧香脆，孩子点免辣骨汤配卤蛋，人均 ¥15）。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>15:30</b></div>
          <div class="slot-body">
            <b>象鼻山公园（1号门进）</b><br>
            全面免费开放。从爱情岛平缓栈道进入，初秋漓江水清浅，带小孩在浅滩观察天然象鼻吸水奇观，推车畅通无阻。<br>
            <span style="font-size:0.8rem;color:var(--ink3)">📷 机位提示：爱情岛临江滩涂（16:30 柔和顺光，拍孩子指着大象喝水的合影）。</span>
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>18:00</b></div>
          <div class="slot-body">
            <b>晚餐 · 椿记烧鹅（中山中路店）</b><br>
            桂林老字号家庭首选。招牌烧鹅皮脆肉嫩、大千水豆腐、流沙包无骨无辣，深受孩子喜爱（人均 ¥80）。（更多选择在美食清单）
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>19:30</b></div>
          <div class="slot-body">
            <b>两江四湖日月双塔散步</b><br>
            沿杉湖环湖木栈道夜游，金银双塔倒映水中，晚风轻拂，沿途多长椅可随时停歇。
          </div>
        </div>

        <div class="note-row photo">
          <span class="ic">🛏</span>
          <div><b>住宿：</b>入住桂林漓江大瀑布饭店（中山中路，出门即杉湖，推车极其便捷）。早餐由酒店含早解决。</div>
        </div>
      </div>
    </section>

    <!-- 4. DAY 2 -->
    <section id="day2">
      <div class="day">
        <div class="day-head">
          <div class="day-idx">DAY 02 · 2026-11-18</div>
          <h3>自然地下魔宫 · 芦笛岩与东西巷历史漫步</h3>
          <span class="today-badge">· 今天</span>
        </div>

        <div class="note-row">
          <span class="ic">🧭</span>
          <div><b>今日速览：</b>上午=芦笛岩地下水晶宫探奇；下午=酒店午休充沛精力；傍晚=东西巷古街漫步与登逍遥楼观江景。</div>
        </div>

        <div class="photos">
          <figure>
            <img src="{img_d2_1}" alt="芦笛岩钟乳石奇观" loading="lazy">
            <figcaption>芦笛岩 · 地下恒温水晶宫与钟乳石笋（实景示意）</figcaption>
          </figure>
          <figure>
            <img src="{img_d2_2}" alt="东西巷与逍遥楼" loading="lazy">
            <figcaption>东西巷逍遥楼 · 俯瞰漓江与解放桥（实景示意）</figcaption>
          </figure>
        </div>

        <div class="slot">
          <div class="slot-time"><b>09:00</b></div>
          <div class="slot-body">
            <b>早餐 · 酒店自助早餐</b><br>
            在酒店享用丰富早餐，睡到自然醒，不慌不忙。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>10:00</b></div>
          <div class="slot-body">
            <b>芦笛岩溶洞探秘</b><br>
            打车 15 分钟直达。洞内常年恒温 20℃，步道规整平缓，配专业导游随行讲解石幔石笋，奇幻灯光犹如海底宫殿，全程游玩约 1.5 小时。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>12:30</b></div>
          <div class="slot-body">
            <b>午餐 · 小南国（文明路店）</b><br>
            桂林家常菜招牌。点旱蒸剑骨鱼（无刺软嫩适合儿童）、脆皮烤鸭、拔丝芋头（人均 ¥70）。（更多选择在美食清单）
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>14:30</b></div>
          <div class="slot-body">
            <b>午休蓄力 · 亲子节奏保障</b><br>
            带娃回酒店午休 1.5 小时，大人也趁机小憩，彻底保证下午出游精力。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>16:30</b></div>
          <div class="slot-body">
            <b>东西巷与逍遥楼慢逛</b><br>
            打车至东西巷，青砖黛瓦的明清古巷地面平整；登上逍遥楼二层远眺漓江两岸与解放桥风光。<br>
            <span style="font-size:0.8rem;color:var(--ink3)">📷 机位提示：逍遥楼城楼外侧（17:30 傍晚时分，以红柱灰瓦与漓江水面为背景）。</span>
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>18:30</b></div>
          <div class="slot-body">
            <b>晚餐 · 东西巷老字号传统小吃</b><br>
            品尝老桂林温热板栗羹、马蹄爽、桂花蒸糕，清润可口（人均 ¥30）。
          </div>
        </div>

        <div class="note-row photo">
          <span class="ic">🛏</span>
          <div><b>住宿：</b>续住桂林漓江大瀑布饭店。晚间整理行李，为次日登漓江游船做准备。</div>
        </div>
      </div>
    </section>

    <!-- 5. DAY 3 -->
    <section id="day3">
      <div class="day">
        <div class="day-head">
          <div class="day-idx">DAY 03 · 2026-11-19</div>
          <h3>漓江豪华大船下阳朔 · 入住遇龙河田园秘境</h3>
          <span class="today-badge">· 今天</span>
        </div>

        <div class="note-row">
          <span class="ic">🧭</span>
          <div><b>今日速览：</b>上午=登漓江三星游船顺流观百里画廊；下午=抵达阳朔入住遇龙河畔山水民宿；傍晚=民宿草坪放空看日落。</div>
        </div>

        <div class="photos">
          <figure>
            <img src="{img_d3_1}" alt="漓江三星级游船" loading="lazy">
            <figcaption>漓江三星级游船 · 九马画山与黄布倒影江段（实景示意）</figcaption>
          </figure>
          <figure>
            <img src="{img_d3_2}" alt="遇龙河山水民宿" loading="lazy">
            <figcaption>阳朔遇龙河畔民宿 · 推窗见山草坪度假（实景示意）</figcaption>
          </figure>
        </div>

        <div class="slot">
          <div class="slot-time"><b>08:30</b></div>
          <div class="slot-body">
            <b>早餐 · 酒店自助并退房</b><br>
            吃完早餐退房，网约车 40 分钟直达桂林磨盘山码头。大件行李与婴儿推车直接推上游船客舱。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>09:40</b></div>
          <div class="slot-body">
            <b>漓江三星级游船起航（航程 4 小时）</b><br>
            经杨堤、九马画山、黄布倒影。三层甲板宽阔平稳，客舱空调恒温无风浪。孩子累了在二层软座看绘本，精神好时带上甲板看如画峰林。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>12:30</b></div>
          <div class="slot-body">
            <b>午餐 · 船上享用自备精美烘焙与水果</b><br>
            游船票不含大餐，提前在市区准备好现烤面包、牛奶、水果与坚果，在江面上轻松野餐。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>14:00</b></div>
          <div class="slot-body">
            <b>抵达阳朔龙头山码头 · 接驳入住</b><br>
            民宿专车在码头出口迎候，20 分钟避开西街喧嚣，直达遇龙河腹地度假民宿。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>15:30</b></div>
          <div class="slot-body">
            <b>民宿草坪撒欢 · 大人度假放空</b><br>
            在民宿庭院喝茶看山，带孩子在草坪荡秋千、喂池塘锦鲤，彻底进入大自然松弛状态。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>18:00</b></div>
          <div class="slot-body">
            <b>晚餐 · 望江楼餐馆（遇龙河分店）</b><br>
            必点番茄炖剑骨鱼（叮嘱免辣，无细刺适合孩子）、荔浦芋头煲、清炒南瓜苗（人均 ¥85）。（更多选择在美食清单）
          </div>
        </div>

        <div class="note-row photo">
          <span class="ic">🛏</span>
          <div><b>住宿：</b>入住阳朔霁云上院度假酒店（或水岸山居）。十里画廊遇龙河畔，落地窗直对峰林，安静怡人。</div>
        </div>
      </div>
    </section>

    <!-- 6. DAY 4 -->
    <section id="day4">
      <div class="day">
        <div class="day-head">
          <div class="day-idx">DAY 04 · 2026-11-20</div>
          <h3>遇龙河亲子平缓大筏 · 十里画廊亲子骑行</h3>
          <span class="today-badge">· 今天</span>
        </div>

        <div class="note-row">
          <span class="ic">🧭</span>
          <div><b>今日速览：</b>上午=乘万景码头平缓多座大筏漂流；下午=骥马村农家午餐；傍晚=租亲子电动车慢骑工农桥看晚霞。</div>
        </div>

        <div class="photos">
          <figure>
            <img src="{img_d4_1}" alt="遇龙河万景码头平缓大筏" loading="lazy">
            <figcaption>遇龙河万景码头 · 亲子老少平缓大筏（实景示意）</figcaption>
          </figure>
          <figure>
            <img src="{img_d4_2}" alt="十里画廊工农桥夕阳" loading="lazy">
            <figcaption>十里画廊工农桥 · 凤尾竹与田园日落（实景示意）</figcaption>
          </figure>
        </div>

        <div class="slot">
          <div class="slot-time"><b>09:00</b></div>
          <div class="slot-body">
            <b>早餐 · 民宿田园现熬香粥与点心</b><br>
            在民宿庭院享用热乎的农家小米粥、煎土鸡蛋和玉米，自然醒后悠然出发。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>10:00</b></div>
          <div class="slot-body">
            <b>遇龙河万景码头 · 亲子休闲大筏</b><br>
            水面平缓如镜，两岸凤尾竹低垂。无落差冲坝，全家安全同乘，微风轻拂格外舒适（漂流约 45 分钟）。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>12:00</b></div>
          <div class="slot-body">
            <b>午餐 · 骥马村农家院</b><br>
            竹筒现炖土鸡汤（汤汁清甜开胃）、农家手工香煎豆腐、时令自种蔬菜（人均 ¥60）。（更多选择在美食清单）
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>14:30</b></div>
          <div class="slot-body">
            <b>十里画廊亲子慢骑行</b><br>
            租一辆带儿童安全座椅与头盔的国标亲子电动自行车，沿遇龙河绿道骑行，途经骆驼过江、遇龙水车，田埂常有水牛吃草，童趣十足。<br>
            <span style="font-size:0.8rem;color:var(--ink3)">📷 机位提示：工农桥西侧观景台（16:45 逆光看晚霞峰林倒影）。</span>
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>18:00</b></div>
          <div class="slot-body">
            <b>晚餐 · 喜鹊花园餐厅</b><br>
            阳朔县城外围的花园庭院西餐厅，点番茄肉酱意面、手工玛格丽特披萨与时令鲜果饮，满足小孩口味（人均 ¥90）。
          </div>
        </div>

        <div class="note-row photo">
          <span class="ic">🛏</span>
          <div><b>住宿：</b>续住阳朔遇龙河畔度假民宿。夜间可在大露台与孩子一起数星星。</div>
        </div>
      </div>
    </section>

    <!-- 7. DAY 5 -->
    <section id="day5">
      <div class="day">
        <div class="day-head">
          <div class="day-idx">DAY 05 · 2026-11-21</div>
          <h3>如意峰索道全景 · 兴坪老街20元纸币打卡</h3>
          <span class="today-badge">· 今天</span>
        </div>

        <div class="note-row">
          <span class="ic">🧭</span>
          <div><b>今日速览：</b>上午=如意峰封闭索道登顶赏万峰丛林；下午=兴坪古镇品尝江鲜；傍晚=元宝山拿真钞打卡20元人民币实景。</div>
        </div>

        <div class="photos">
          <figure>
            <img src="{img_d5_1}" alt="如意峰高空索道与玻璃桥" loading="lazy">
            <figcaption>如意峰索道 · 俯瞰喀斯特峰林全景（实景示意）</figcaption>
          </figure>
          <figure>
            <img src="{img_d5_2}" alt="兴坪20元人民币实景" loading="lazy">
            <figcaption>兴坪元宝山 · 拿20元人民币对景打卡（实景示意）</figcaption>
          </figure>
        </div>

        <div class="slot">
          <div class="slot-time"><b>09:00</b></div>
          <div class="slot-body">
            <b>早餐 · 民宿特色桂林米粉</b><br>
            民宿管家现煮温热骨汤米粉，配香脆黄豆与葱花，暖胃舒坦。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>10:00</b></div>
          <div class="slot-body">
            <b>如意峰索道景区</b><br>
            包车 25 分钟前往。全封闭索道直达山顶，山顶为平缓无障碍高空栈道与索桥（婴儿车畅行）。登高俯瞰千峰环抱，视觉体验极具震撼。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>13:00</b></div>
          <div class="slot-body">
            <b>午餐 · 兴坪老街坊土菜馆</b><br>
            清蒸漓江白条鱼、农家蒸水蛋、黄豆焖土鸭，清爽适口（人均 ¥65）。（更多选择在美食清单）
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>14:30</b></div>
          <div class="slot-body">
            <b>20 元人民币实景打卡</b><br>
            漫步至朝板山码头观景台，掏出一张崭新 20 元人民币纸币，带孩子现场比对眼前真实山峦，寓教于乐。<br>
            <span style="font-size:0.8rem;color:var(--ink3)">📷 机位提示：朝板山元宝山观景台（下午顺光，纸币与山景自然重合）。</span>
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>18:00</b></div>
          <div class="slot-body">
            <b>晚餐 · 富安码头柴火鼎锅饭</b><br>
            金黄香脆锅巴配腊味与土鸡肉，香味扑鼻，全家饱食暖心（人均 ¥75）。
          </div>
        </div>

        <div class="note-row photo">
          <span class="ic">🛏</span>
          <div><b>住宿：</b>续住阳朔遇龙河畔度假民宿。打包整理行李，准备次日愉快返程。</div>
        </div>
      </div>
    </section>

    <!-- 8. DAY 6 -->
    <section id="day6">
      <div class="day">
        <div class="day-head">
          <div class="day-idx">DAY 06 · 2026-11-22</div>
          <h3>睡到自然醒 · 漓江晨雾 · 悠闲返深</h3>
          <span class="today-badge">· 今天</span>
        </div>

        <div class="note-row">
          <span class="ic">🧭</span>
          <div><b>今日速览：</b>上午=遇龙河畔晨间散步与自然醒慢早餐；下午=专车送至阳朔高铁站乘高铁返回深圳北站。</div>
        </div>

        <div class="photos">
          <figure>
            <img src="{img_d6_1}" alt="遇龙河水墨晨雾" loading="lazy">
            <figcaption>遇龙河晨景 · 雾霭轻笼与凤尾竹林（实景示意）</figcaption>
          </figure>
          <figure>
            <img src="{img_d6_2}" alt="阳朔返程深圳高铁" loading="lazy">
            <figcaption>悠闲返程 · 满载山水回忆平安回深（实景示意）</figcaption>
          </figure>
        </div>

        <div class="slot">
          <div class="slot-time"><b>09:00</b></div>
          <div class="slot-body">
            <b>早餐 · 庭院慢享晨光早餐</b><br>
            不设闹钟睡到自然醒。在民宿庭院品尝现磨豆浆、阳朔手工油茶点心，享受最后的宁静山水。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>10:00</b></div>
          <div class="slot-body">
            <b>遇龙河畔亲子拾趣散步</b><br>
            在民宿周边小径漫步，带孩子观察凤尾竹与稻田，拾捡落叶留作旅行纪念。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>11:30</b></div>
          <div class="slot-body">
            <b>午餐 · 民宿温热便餐并退房</b><br>
            在民宿享用原汤土鸡丝面或排骨汤饭（人均 ¥40），退房装车。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>12:30</b></div>
          <div class="slot-body">
            <b>专车前往阳朔高铁站</b><br>
            专车约 45 分钟直达阳朔站候车，车程顺畅无压力。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>14:00</b></div>
          <div class="slot-body">
            <b>搭乘高铁返深 · 抵达深圳北站</b><br>
            乘坐高铁（直达或经广州南中转）返回深圳北站，行程圆满结束。
          </div>
        </div>
        <div class="slot">
          <div class="slot-time"><b>18:30</b></div>
          <div class="slot-body">
            <b>晚餐 · 深圳温暖到家享用家常晚餐</b><br>
            回到深圳温馨家中，整理行李照片，孩子早睡安歇。
          </div>
        </div>

        <div class="note-row photo">
          <span class="ic">🏠</span>
          <div><b>返程：</b>平平安安到家，山水之旅圆满收官！</div>
        </div>
      </div>
    </section>

    <!-- 9. BOOST -->
    <section id="boost">
      <div class="eyebrow">BOOST · 备选与特殊时段</div>
      <h2>特殊时段玩法与加餐备选</h2>
      <p class="lead">专为精力充沛或有特殊摄影爱好的家庭准备，不强求全员参加，谁愿起谁去。</p>

      <div class="card">
        <h3>⏰ 特殊时段玩法清单</h3>
        <table class="tb">
          <thead>
            <tr><th>玩法项目</th><th>最佳时点</th><th>为什么非得那个点</th><th>作息代价与归入</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><b>遇龙河水墨晨雾</b></td>
              <td>06:45–07:30</td>
              <td>初秋水汽遇晨冷凝结成轻纱白雾，宛如水墨长卷，日出后即散</td>
              <td>需 06:30 早起，仅在民宿露台或河边看，归入【早起包】，不影响全队 10 点自然醒主线</td>
            </tr>
            <tr>
              <td><b>桂林千古情演出</b></td>
              <td>19:30–20:30</td>
              <td>大型室内外声光电剧场，儿童互动多（适合 5 岁以上大孩子）</td>
              <td>晚间回酒店约 21:30，归入【夜游包备选】；若孩子年龄过小容易受暗光惊吓，则建议放弃</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 10. TICKET -->
    <section id="ticket">
      <div class="eyebrow">TICKET · 门票与预约</div>
      <h2>景区门票与实名预约表</h2>
      <p class="lead">所有门票价格均为 2026-10-09 最新实查时戳，官方渠道优先，无任何水分。</p>

      <table class="tb">
        <thead>
          <tr><th>景点项目</th><th>官方价格 (2026-10-09 实查)</th><th>预约放票渠道</th><th>儿童优惠政策与关键门槛</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><b>象鼻山公园</b></td>
            <td><b>免费 ¥0</b></td>
            <td>微信小程序【象山景区】提前1-3天预约</td>
            <td>全员免票，刷预约二维码直接入园</td>
          </tr>
          <tr>
            <td><b>漓江三星级游船</b><br>(磨盘山→阳朔)</td>
            <td>成人 <b>¥215</b><br>儿童 <b>¥108</b></td>
            <td>小程序【桂林漓江商城】/ 微信【漓江售票处】提前3-5天实名预约</td>
            <td>1.2米以下免票无独立座；1.2-1.5米享半价儿童票；航程约4小时，票不含正餐（需自备）</td>
          </tr>
          <tr>
            <td><b>芦笛岩</b></td>
            <td>成人 <b>¥90</b> (网购约 ¥75-80)<br>儿童 <b>¥45</b></td>
            <td>美团 / 携程 / 官方公众号可提前预订</td>
            <td>1.2米以下或6周岁以下儿童免票；洞内恒温20℃，游览约1小时</td>
          </tr>
          <tr>
            <td><b>遇龙河万景休闲大筏</b></td>
            <td>约 <b>¥45/人</b></td>
            <td>微信公众号【遇龙河】每晚20:00放次日票</td>
            <td><b>亲子首选</b>：平稳无冲坝，<b>允许1米以下儿童乘坐</b>，全家同筏</td>
          </tr>
          <tr>
            <td><b>阳朔如意峰索道</b></td>
            <td>成人 <b>¥208-240</b> (含往返索道+玻璃桥)</td>
            <td>美团 / 携程 / 官方小程序提前1天购票享折扣</td>
            <td>6-14周岁或1.2-1.5米享半价优惠 ¥108（2026-10-09 查）；封闭索道直达山顶，推车平缓无障碍</td>
          </tr>
          <tr>
            <td><b>兴坪20元人民币展台</b></td>
            <td><b>免费 ¥0</b></td>
            <td>公共开放式江畔观景台</td>
            <td>无需购票，朝板山/元宝山码头边随时可打卡</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- 11. TIPS -->
    <section id="tips">
      <div class="eyebrow">TIPS · 真实场景避雷</div>
      <h2>提示与避雷指南</h2>
      <p class="lead">基于亲子真实出行翻车血泪史总结，分为防套路避雷组与贴身实用提示组。</p>

      <div class="tips">
        <div class="tip">
          <div>
            <b>⚠️ 遇龙河双人冲坝竹筏儿童限高红线：</b><br>
            金龙桥至旧县等双人竹筏航线<b>严格严禁 1 米以下儿童乘搭</b>，且每筏严格限乘 2 人不得抱小孩加座。现场绝无商量余地，黄牛“加钱走后门”全属骗局。两大一小请坚决认准【万景码头休闲多座大筏】，水流平稳无冲坝，合法合规老少皆宜。
          </div>
        </div>
        <div class="tip">
          <div>
            <b>⚠️ 啤酒鱼点单套路与鱼刺安全：</b><br>
            阳朔西街很多排档拉客宣称“啤酒鱼 38 元/斤”，结账时常按大鱼整条算动辄数百元。且草鱼/鲤鱼小细刺多，极易卡到孩子咽喉。必须去明码标价名店，<b>必点无细刺的“剑骨鱼（或毛骨鱼）”</b>，并交待厨房“做番茄味或原汁清蒸，做免辣”。
          </div>
        </div>
        <div class="tip">
          <div>
            <b>⚠️ 街头野导拉客绝不理睬：</b><br>
            阳朔西街路口常有骑电动车人员兜售“便宜船票、10元看漓江、半价银子岩”，多为拉去野码头或强制进店。一律礼貌摇头不理，所有门票在官方公众号自购。
          </div>
        </div>
        <div class="tip">
          <div>
            <b>🌧️ 全程雨天备选方案（雨天也是正选）：</b><br>
            初秋偶遇小雨是漓江烟雨美景，若遇持续阵雨，果断将户外骑行切换为【芦笛岩地下溶洞】或在阳朔入驻的亲子度假民宿私家茶室手作桂花糕、听雨看山，室内恒温不折腾。
          </div>
        </div>
        <div class="tip">
          <div>
            <b>📌 婴儿推车与上下船提示：</b><br>
            象鼻山、东西巷、芦笛岩、如意峰索道上站皆推车平缓；仅漓江游船上下码头有十余级石阶梯，准备折叠轻便伞车一人可单手提起。
          </div>
        </div>
      </div>
    </section>

    <!-- 12. STAY -->
    <section id="stay">
      <div class="eyebrow">STAY · 住宿必答</div>
      <h2>全案住宿推荐与选房逻辑</h2>
      <p class="lead">全程坚决不住吵闹的阳朔西街酒吧区。前 2 晚住桂林两江四湖边，后 3 晚住遇龙河十里画廊内，动线顺畅。</p>

      <div class="card">
        <h3>1. 桂林市区（Day 1–2，住 2 晚）</h3>
        <p><b>首选：桂林漓江大瀑布饭店</b>（参考价：¥450–650/晚）<br>
        <b>为什么适合两大一小：</b>老牌国宾级老字号，紧邻杉湖与象鼻山，出门即是步行街与湖畔栈道。带恒温室内泳池，婴儿床围与儿童拖鞋齐全，推车出行零门槛。<br>
        <b>备选：</b>桂林喜来登饭店（一线漓江江景，服务标准规范）。</p>
      </div>

      <div class="card">
        <h3>2. 阳朔遇龙河畔（Day 3–5，住 3 晚）</h3>
        <p><b>首选：阳朔霁云上院度假酒店 / 水岸山居亲子民宿</b>（参考价：¥700–1100/晚）<br>
        <b>为什么适合两大一小：</b>坐落于遇龙河十里画廊田园核心区，开门推窗即是喀斯特峰林与稻田。自带数百平米开阔草坪、儿童秋千秋千池与私家无边泳池，管家提供贴心接送与暖心服务。<br>
        <b>备选：</b>遇龙河胜地度假山庄（老牌水岸庭院）。</p>
      </div>

      <div class="warn-line">
        <b>💡 订房问三样：</b>1. 确认亲子大床房是否有床围防护栏；2. 确认是否提供儿童专用牙刷与小拖鞋；3. 确认退房时间（通常为 12:00）。
      </div>
    </section>

    <!-- 13. COST -->
    <section id="cost">
      <div class="eyebrow">COST · 全案预算</div>
      <h2>全案预算清单（两大一小）</h2>
      <p class="lead">纯玩度假品质档，透明诚实，将交通、门票、住宿、餐饮及隐藏成本全口径列清。</p>

      <div class="stats">
        <div class="stat">
          <div class="n">¥9,350</div>
          <div class="l">预估总预算（两大一小）</div>
        </div>
        <div class="stat">
          <div class="n">¥3,116</div>
          <div class="l">人均预估消费</div>
        </div>
        <div class="stat">
          <div class="n">6天5晚</div>
          <div class="l">品质慢度假周期</div>
        </div>
      </div>

      <table class="tb" style="margin-top:20px">
        <thead>
          <tr><th>支出类别</th><th>项目明细</th><th>两大一小预估金额</th><th>备注说明</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><b>大交通</b></td>
            <td>深圳北 ↔ 桂林北/阳朔 高铁往返</td>
            <td>¥1,700</td>
            <td>成人二等座 ¥212×4程，儿童依身高享半价/免票</td>
          </tr>
          <tr>
            <td><b>市内交通</b></td>
            <td>网约车 + 漓江三星游船 + 阳朔包车 + 电动车</td>
            <td>¥1,100</td>
            <td>含漓江三星大船（2大1小约 ¥538）+ 打车与专车接驳</td>
          </tr>
          <tr>
            <td><b>品质住宿</b></td>
            <td>桂林市区 2 晚 + 阳朔遇龙河民宿 3 晚</td>
            <td>¥3,600</td>
            <td>桂林约 ¥550×2晚 + 阳朔亲子度假房约 ¥850×3晚</td>
          </tr>
          <tr>
            <td><b>景区门票</b></td>
            <td>芦笛岩 + 如意峰索道 + 遇龙河大筏</td>
            <td>¥750</td>
            <td>象鼻山与兴坪观景台免费；如意峰及大筏家庭票</td>
          </tr>
          <tr>
            <td><b>餐饮美馔</b></td>
            <td>6 天正餐（老字号烧鹅、家常菜、农家土鸡）</td>
            <td>¥1,800</td>
            <td>平均每日约 ¥300，包含早茶、正餐与水果甜品</td>
          </tr>
          <tr>
            <td><b>隐藏成本行</b></td>
            <td>婴儿车行李短驳、景区鞋套、小吃零食、电瓶车充电</td>
            <td>¥400</td>
            <td><b>隐藏成本：</b>杂项小费、景区拍照、行李短驳与应急备用</td>
          </tr>
          <tr>
            <td><b>总计</b></td>
            <td><b>两大一小 6 天 5 晚全包总计</b></td>
            <td><b>约 ¥9,350</b></td>
            <td>体验品质舒适档，无强制隐形消费</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- 14. SOS -->
    <section id="sos">
      <div class="eyebrow">SOS · 应急与兜底</div>
      <h2>安全兜底与应急联络</h2>
      <p class="lead">带娃出行安全永远第一位，紧急医疗、医院与求助通道随时备查。</p>

      <div class="sos-grid">
        <div class="sos">
          <h4>🏥 桂林市区医疗救助</h4>
          <p><b>桂林医学院附属医院（三甲综合）</b><br>
          地址：象山区乐群路 15 号<br>
          急诊电话：0773-2822120 / 拨打 120<br>
          距市区酒店仅 10 分钟车程，儿科急诊 24 小时在岗。</p>
        </div>
        <div class="sos">
          <h4>🏥 阳朔县域医疗兜底</h4>
          <p><b>阳朔县人民医院（二级甲等综合）</b><br>
          地址：阳朔县城西路 120 号<br>
          急诊电话：0773-8822416 / 拨打 120<br>
          距遇龙河十里画廊约 15 分钟车程，处理水土不服、外伤。</p>
        </div>
        <div class="sos">
          <h4>🛡️ 肠胃突发与求助通道</h4>
          <p>随身携带小儿蒙脱石散与口服补液盐；如遇水上突发情况听从码头工作人员指挥；阳朔旅游咨询投诉：0773-8828779。</p>
        </div>
      </div>
    </section>

    <!-- 15. EAT -->
    <section id="eat">
      <div class="eyebrow">EAT · 美食清单</div>
      <h2>全行程美食地图</h2>
      <p class="lead">按行程时间线排布，每餐精心挑选兼顾大人地道风味与小孩口味的品质餐厅。</p>

      <table class="tb">
        <thead>
          <tr><th>餐段</th><th>地界</th><th>店名与地址</th><th>推荐必点菜（亲子指南）</th><th>人均参考</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><b>D1 早餐</b> · 随意</td>
            <td>深圳北</td>
            <td>高铁站内品牌烘焙 / 广式早点</td>
            <td>温热鲜奶、蛋挞、叉烧包</td>
            <td>¥25</td>
          </tr>
          <tr>
            <td><b>D1 午餐</b></td>
            <td>桂林市区</td>
            <td><b>明桂米粉（中山中路店）</b><br>象山区中山中路 18 号</td>
            <td>原味卤菜粉（锅烧香脆，孩子免辣加骨汤卤蛋）</td>
            <td>¥15</td>
          </tr>
          <tr>
            <td><b>D1 晚餐</b></td>
            <td>桂林市区</td>
            <td><b>椿记烧鹅（中山中路店）</b><br>象山区中山中路 2 号</td>
            <td>招牌脆皮烧鹅、大千水豆腐、流沙包、菠萝包</td>
            <td>¥80</td>
          </tr>
          <tr>
            <td><b>D2 早餐</b> · 随意</td>
            <td>桂林市区</td>
            <td>酒店全日制自助餐厅</td>
            <td>现煎荷包蛋、清粥小菜、热牛奶、水果麦片</td>
            <td>酒店含早</td>
          </tr>
          <tr>
            <td><b>D2 午餐</b></td>
            <td>桂林市区</td>
            <td><b>小南国（文明路店）</b><br>象山区文明路 3 号</td>
            <td>旱蒸剑骨鱼（无细刺软嫩）、脆皮烤鸭、拔丝芋头</td>
            <td>¥70</td>
          </tr>
          <tr>
            <td><b>D2 晚餐</b></td>
            <td>桂林市区</td>
            <td><b>正阳步行街老字号糖水</b><br>正阳步行街内</td>
            <td>桂林传统热板栗羹、马蹄爽、桂花蒸米糕</td>
            <td>¥30</td>
          </tr>
          <tr>
            <td><b>D3 早餐</b> · 随意</td>
            <td>桂林市区</td>
            <td>酒店自助早点</td>
            <td>现煮桂林米粉、蒸玉米、手工包子</td>
            <td>酒店含早</td>
          </tr>
          <tr>
            <td><b>D3 午餐</b></td>
            <td>漓江游船</td>
            <td>游船客舱江上野餐</td>
            <td>前一天市区购买的现烤软欧包、酸奶、香蕉</td>
            <td>¥35</td>
          </tr>
          <tr>
            <td><b>D3 晚餐</b></td>
            <td>阳朔遇龙河</td>
            <td><b>望江楼餐馆（遇龙河店）</b><br>阳朔十里画廊沿岸</td>
            <td>番茄炖剑骨鱼（叮嘱免辣）、荔浦芋头煲、清炒南瓜苗</td>
            <td>¥85</td>
          </tr>
          <tr>
            <td><b>D4 早餐</b> · 随意</td>
            <td>阳朔民宿</td>
            <td>民宿庭院早餐</td>
            <td>农家小米粥、柴火煮鸡蛋、香甜红薯</td>
            <td>民宿含早</td>
          </tr>
          <tr>
            <td><b>D4 午餐</b></td>
            <td>阳朔骥马村</td>
            <td><b>朝阳农家土鸡馆</b><br>阳朔骥马村村道旁</td>
            <td>竹筒清炖土鸡汤（汤味极鲜甜）、农家手工香煎豆腐</td>
            <td>¥60</td>
          </tr>
          <tr>
            <td><b>D4 晚餐</b></td>
            <td>阳朔县城外</td>
            <td><b>喜鹊花园餐厅</b><br>阳朔县城外围花园庭院</td>
            <td>手工玛格丽特披萨、番茄肉酱意面、鲜榨西瓜汁</td>
            <td>¥90</td>
          </tr>
          <tr>
            <td><b>D5 早餐</b> · 随意</td>
            <td>阳朔民宿</td>
            <td>民宿现煮米粉</td>
            <td>温热高汤米粉配酥脆黄豆与葱花</td>
            <td>民宿含早</td>
          </tr>
          <tr>
            <td><b>D5 午餐</b></td>
            <td>兴坪古镇</td>
            <td><b>老街坊土菜馆</b><br>兴坪古镇老街中心</td>
            <td>清蒸漓江白条鱼、农家蒸水蛋、黄豆焖土鸭</td>
            <td>¥65</td>
          </tr>
          <tr>
            <td><b>D5 晚餐</b></td>
            <td>阳朔县城</td>
            <td><b>富安码头特色柴火鼎锅饭</b><br>阳朔滨江路码头旁</td>
            <td>金黄香脆鼎锅饭、腊味土鸡排骨煲</td>
            <td>¥75</td>
          </tr>
          <tr>
            <td><b>D6 早餐</b> · 随意</td>
            <td>阳朔民宿</td>
            <td>庭院慢调早餐</td>
            <td>现磨豆浆、手工油茶小点心、时令水果</td>
            <td>民宿含早</td>
          </tr>
          <tr>
            <td><b>D6 午餐</b></td>
            <td>阳朔民宿</td>
            <td>民宿简餐便饭</td>
            <td>原汤鸡丝面、清炒小青菜</td>
            <td>¥40</td>
          </tr>
          <tr>
            <td><b>D6 晚餐</b></td>
            <td>深圳家中</td>
            <td>温暖到家家常便饭</td>
            <td>清淡家常热汤、米饭</td>
            <td>家中</td>
          </tr>
        </tbody>
      </table>

      <div class="card" style="margin-top:20px">
        <h3>✨ 美食清单「升级体验」子表（仪式感选项）</h3>
        <table class="tb">
          <thead>
            <tr><th>餐厅名称</th><th>地界位置</th><th>升级体验亮点（写体验不写菜名）</th><th>人均参考</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><b>糖舍 · 1969 餐厅</b></td>
              <td>阳朔工农桥附近</td>
              <td>老糖厂工业遗址与现代建筑交织，在漓江峰林倒影中享用黑松露私房菜与法式甜点，全家度假仪式感拉满</td>
              <td>¥220–300</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 16. GIFT -->
    <section id="gift">
      <div class="eyebrow">GIFT · 特产三问</div>
      <h2>特产手信与伴手礼指南</h2>
      <p class="lead">不买景区门口三无特产，选品质可靠、便于携带的桂林地道风物。</p>

      <table class="tb">
        <thead>
          <tr><th>特产类别</th><th>推荐好物</th><th>参考价位</th><th>正规购买地点</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><b>儿童小零食</b></td>
            <td>荔浦芋头条 / 香脆芋头干</td>
            <td>约 ¥15–25/袋</td>
            <td>桂林市区微笑堂地下大超市</td>
          </tr>
          <tr>
            <td><b>清雅茶饮</b></td>
            <td>头采桂花干 / 金桂蜜酱</td>
            <td>约 ¥25–40/罐</td>
            <td>桂林市区正规特产店 / 微笑堂商厦</td>
          </tr>
          <tr>
            <td><b>长辈伴手礼</b></td>
            <td>陶瓶装桂林三花酒 / 桂花陈酿</td>
            <td>约 ¥50–120/瓶</td>
            <td>微笑堂地下超市明码标价专柜</td>
          </tr>
          <tr>
            <td><b>清喉润肺</b></td>
            <td>冻干大罗汉果（绒毛饱满）</td>
            <td>约 ¥6–10/颗</td>
            <td>微笑堂超市专柜，密封整盒包装</td>
          </tr>
        </tbody>
      </table>

      <div class="warn-line" style="margin-top:16px">
        <b>⚠️ 避坑提醒：</b>阳朔西街或各景区出口摊位上“10元4盒/5盒”的塑封桂花糕全为香精防腐剂淀粉混合物，口感发硬，切勿购买！一律在桂林市区大型超市一站式选购并快递包邮到家。
      </div>
    </section>

    <!-- FOOTER -->
    <footer style="padding:64px 0 80px;text-align:center">
      <h2>桂林阳朔路书 · 亲子慢游版</h2>
      <p>深圳北出发 · 2026-11-17 至 11-22 · 两大一小家庭度假<br>本地单文件 · 无外部依赖 · 断网可打开<br>信息 2026-10-09 联网实查 · 未核实项已标注</p>
      <p>配图：全册 12 张矢量手绘地标示意插图，离线内嵌；图源 自绘矢量示意<br>自绘示意图说明：非等比例、仅供参考</p>
      <p style="margin-top:18px;font-weight:700">方案仅供参考——安全和开心，才是最重要的。🌕</p>
    </footer>

  </div>
</main>

<button class="backtop" id="backtop" aria-label="回到顶部">↑</button>

<script>
(function(){{
  "use strict";

  /* ---------- 1. 当日模式：按今天日期高亮对应行程日 ---------- */
  var TRIP = {{ 
    "2026-11-17":"day1", 
    "2026-11-18":"day2", 
    "2026-11-19":"day3", 
    "2026-11-20":"day4", 
    "2026-11-21":"day5",
    "2026-11-22":"day6"
  }};
  function todayStr(){{
    var d = new Date();
    var m = ("0"+(d.getMonth()+1)).slice(-2), day = ("0"+d.getDate()).slice(-2);
    return d.getFullYear()+"-"+m+"-"+day;
  }}
  var todayId = TRIP[todayStr()];
  if (todayId){{
    var sec = document.getElementById(todayId);
    if (sec){{
      var card = sec.querySelector(".day");
      if (card) card.classList.add("today");
      var navA = document.querySelector('.side nav a[href="#'+todayId+'"]');
      if (navA) navA.innerHTML = navA.textContent + ' · 今天';
      function jumpToday(){{ lockNav(todayId); sec.scrollIntoView({{behavior:"instant", block:"start"}}); }}
      if (document.readyState === "complete"){{ setTimeout(jumpToday, 300); }}
      else {{ window.addEventListener("load", function(){{ setTimeout(jumpToday, 300); }}); }}
    }}
  }} else {{
    var prep = document.getElementById("prepCard");
    if (prep && todayStr() < "2026-11-17") prep.style.border = "2px solid var(--accent)";
  }}

  /* ---------- 2. 字号三档（记忆） ---------- */
  var FONTS = ["17px","19px","21px"];
  var fi = 1;
  try {{ fi = Math.max(0, Math.min(2, parseInt(localStorage.getItem("gl_font")||"1",10)||0)); }} catch(e){{}}
  function applyFont(){{ document.documentElement.style.setProperty("--fs", FONTS[fi]); }}
  applyFont();
  function saveFont(){{ try{{ localStorage.setItem("gl_font", String(fi)); }}catch(e){{}} }}
  document.getElementById("fontInc").addEventListener("click", function(){{ if(fi<2){{fi++;applyFont();saveFont();}} }});
  document.getElementById("fontDec").addEventListener("click", function(){{ if(fi>0){{fi--;applyFont();saveFont();}} }});

  /* ---------- 3. 打印 ---------- */
  document.getElementById("printBtn").addEventListener("click", function(){{ window.print(); }});

  /* ---------- 4. 勾选清单（记忆） ---------- */
  document.querySelectorAll(".check li").forEach(function(li, i){{
    var box = li.querySelector("input");
    var key = "gl_chk_" + box.id;
    try {{ box.checked = localStorage.getItem(key) === "1"; }} catch(e){{}}
    if (box.checked) li.classList.add("done");
    li.addEventListener("click", function(ev){{
      if (ev.target.tagName !== "INPUT"){{ box.checked = !box.checked; }}
      li.classList.toggle("done", box.checked);
      try{{ localStorage.setItem(key, box.checked ? "1" : "0"); }}catch(e){{}}
    }});
  }});

  /* ---------- 5. 滚动监听：侧栏高亮 + 入场动效 ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".side nav a"));
  var secs = Array.prototype.slice.call(document.querySelectorAll("main section"));
  var navLock = null, lockTimer = null;
  function setOn(id){{
    navLinks.forEach(function(a){{ a.classList.toggle("on", a.getAttribute("href") === "#"+id); }});
  }}
  function lockNav(id){{
    navLock = id; setOn(id);
    if (lockTimer) clearTimeout(lockTimer);
    lockTimer = setTimeout(function(){{ navLock = null; }}, 1200);
  }}
  navLinks.forEach(function(a){{
    a.addEventListener("click", function(){{ lockNav((a.getAttribute("href") || "").slice(1)); }});
  }});
  var io = new IntersectionObserver(function(entries){{
    entries.forEach(function(en){{
      if (en.isIntersecting){{
        en.target.classList.add("in");
        if (!navLock) setOn(en.target.id);
      }}
    }});
  }}, {{ rootMargin: "-12% 0px -78% 0px" }});
  secs.forEach(function(s){{ io.observe(s); }});

  /* ---------- 6. 返回顶部 ---------- */
  var bt = document.getElementById("backtop");
  window.addEventListener("scroll", function(){{
    bt.classList.toggle("show", window.scrollY > 600);
  }}, {{ passive:true }});
  bt.addEventListener("click", function(){{ window.scrollTo({{ top:0, behavior:"smooth" }}); }});
}})();
</script>
<script>
/* 兜底：若上方脚本报错导致入场动效未初始化，3 秒后强制显示全部内容 */
setTimeout(function(){{
  if (!document.querySelector('main section.in')){{
    document.querySelectorAll('main section').forEach(function(s){{ s.classList.add('in'); }});
  }}
}}, 3000);
</script>
</body>
</html>
"""

output_path = "D:/Documents/Github/daily-notes/路书_桂林阳朔_v1.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_text)

print("Successfully written to:", output_path)
