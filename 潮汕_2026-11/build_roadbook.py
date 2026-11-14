# -*- coding: utf-8 -*-
"""潮汕 4 天 3 晚 · 一家三口（自驾版）单文件路书生成器。

版式 CSS / 交互 JS 逐字取自 jianhao-travel-planner 的基准骨架，
正文为本趟内容；配图为手绘 SVG 示意（非实景照片），base64 内嵌，断网可开。
改事实请先改 路书_潮汕_v1.md，再同步本脚本 CONTENT 部分重新生成。
"""
import base64
import pathlib
import re

HERE = pathlib.Path(__file__).parent
SKILL = pathlib.Path(r"C:\Users\byhoo\.workbuddy\skills\jianhao-travel-planner")
SKEL = (SKILL / "assets" / "路书_基准骨架.html").read_text(encoding="utf-8")

CSS = re.search(r'<style id="skeleton-css">[\s\S]*?</style>', SKEL).group(0)
JS_ALL = re.search(r'(<script>\s*\(function\(\)\{[\s\S]*?\}\)\(\);\s*</script>\s*<script>[\s\S]*?</script>)\s*</body>', SKEL).group(1)
JS_ALL = JS_ALL.replace(
    '{ "2026-10-01":"day1", "2026-10-02":"day2", "2026-10-03":"day3", "2026-10-04":"day4", "2026-10-05":"day5" }',
    '{ "2026-11-17":"day1", "2026-11-18":"day2", "2026-11-19":"day3", "2026-11-20":"day4" }'
).replace('"2026-10-01"', '"2026-11-17"')
JS_ALL = JS_ALL.replace('__CITY___font', 'csh_font').replace('__CITY___chk_', 'csh_chk_')


def b64(svg):
    return base64.b64encode(svg.encode("utf-8")).decode("ascii")


def fig(title, sub, kind, hue):
    """手绘地标示意插画，统一画幅 720x480，非实景。"""
    sky = {"green": "#DCE9DF", "blue": "#DDEAF3", "amber": "#F3E7CE", "night": "#26313B"}[hue]
    land = {"green": "#9DBBA4", "blue": "#A9C9DC", "amber": "#D7C49A", "night": "#3A4A50"}[hue]
    ink = "#2F5D43" if hue != "night" else "#E9DFC7"
    body = {
        "bridge": (
            f'<rect x="0" y="300" width="720" height="180" fill="{land}"/>'
            '<path d="M0 300 Q180 288 360 300 T720 300" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".6"/>'
            '<g fill="#8B6A45"><rect x="90" y="252" width="18" height="60"/><rect x="210" y="252" width="18" height="60"/>'
            '<rect x="330" y="252" width="18" height="60"/><rect x="450" y="252" width="18" height="60"/>'
            '<rect x="570" y="252" width="18" height="60"/></g>'
            '<path d="M60 250 L660 250" stroke="#6E5237" stroke-width="9"/>'
            '<g fill="#C8764A"><path d="M170 210 h80 l-10 40 h-60 z"/><path d="M350 200 h90 l-12 50 h-66 z"/>'
            '<path d="M520 215 h70 l-8 35 h-54 z"/></g>'
            '<g fill="#6E5237"><rect x="205" y="248" width="6" height="14"/><rect x="390" y="248" width="6" height="14"/></g>'
            '<path d="M270 262 q30 22 60 0 q30 -22 60 0" fill="none" stroke="#C8764A" stroke-width="6"/>'
        ),
        "arch": (
            f'<rect x="0" y="330" width="720" height="150" fill="{land}"/>'
            '<g fill="#C8764A"><rect x="120" y="150" width="26" height="190"/><rect x="574" y="150" width="26" height="190"/>'
            '<rect x="90" y="140" width="540" height="22"/><rect x="110" y="190" width="500" height="16"/>'
            '<rect x="130" y="238" width="460" height="14"/></g>'
            '<g fill="#8B6A45"><rect x="60" y="270" width="90" height="70"/><rect x="570" y="270" width="90" height="70"/></g>'
            '<g fill="#EFE7D4"><rect x="180" y="278" width="70" height="62"/><rect x="470" y="278" width="70" height="62"/></g>'
            '<path d="M0 340 h720" stroke="#8B6A45" stroke-width="4"/>'
        ),
        "lighthouse": (
            f'<rect x="0" y="290" width="720" height="190" fill="{land}"/>'
            '<path d="M0 250 Q180 238 360 250 T720 250" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".55"/>'
            '<path d="M0 190 L720 190" stroke="#8B6A45" stroke-width="7"/>'
            '<g fill="#8B6A45"><rect x="120" y="190" width="12" height="110"/><rect x="300" y="190" width="12" height="110"/>'
            '<rect x="480" y="190" width="12" height="110"/><rect x="640" y="190" width="12" height="110"/></g>'
            '<path d="M520 290 L548 120 L576 290 Z" fill="#F4F1E8" stroke="#C8764A" stroke-width="4"/>'
            '<rect x="536" y="172" width="24" height="30" fill="#C8764A"/><rect x="536" y="232" width="24" height="30" fill="#C8764A"/>'
            '<rect x="540" y="104" width="16" height="20" fill="#E0B25A"/>'
            '<circle cx="548" cy="96" r="13" fill="#F6D98A"/>'
        ),
        "bay": (
            f'<rect x="0" y="260" width="720" height="220" fill="{land}"/>'
            '<path d="M0 250 Q200 200 400 250 T720 240 L720 330 L0 330 Z" fill="#BBD9E6"/>'
            '<path d="M0 330 Q220 290 430 330 T720 320 L720 480 L0 480 Z" fill="#EBDCB8"/>'
            '<circle cx="590" cy="120" r="52" fill="#F0C879"/>'
            '<g fill="#FFFFFF" opacity=".8"><circle cx="170" cy="120" r="24"/><circle cx="205" cy="112" r="30"/><circle cx="242" cy="122" r="22"/></g>'
            '<path d="M330 200 l40 -70 l40 70" fill="none" stroke="#8B6A45" stroke-width="6"/>'
            '<path d="M370 130 v70" stroke="#8B6A45" stroke-width="4"/>'
        ),
        "arcade": (
            f'<rect x="0" y="360" width="720" height="120" fill="{land}"/>'
            '<g fill="#D9C5A4"><rect x="40" y="140" width="130" height="220"/><rect x="180" y="120" width="130" height="240"/>'
            '<rect x="320" y="145" width="130" height="215"/><rect x="460" y="125" width="130" height="235"/>'
            '<rect x="600" y="150" width="110" height="210"/></g>'
            '<g fill="#8B6A45"><path d="M60 250 a45 45 0 0 1 90 0 v40 h-90 z"/>'
            '<path d="M200 240 a45 45 0 0 1 90 0 v50 h-90 z"/><path d="M340 250 a45 45 0 0 1 90 0 v40 h-90 z"/>'
            '<path d="M480 240 a45 45 0 0 1 90 0 v50 h-90 z"/><path d="M615 255 a40 40 0 0 1 80 0 v35 h-80 z"/></g>'
            '<g fill="#F4EEDC"><rect x="72" y="310" width="66" height="50"/><rect x="212" y="310" width="66" height="50"/>'
            '<rect x="352" y="310" width="66" height="50"/><rect x="492" y="310" width="66" height="50"/></g>'
        ),
        "hotpot": (
            f'<rect x="0" y="0" width="720" height="480" fill="{sky}"/>'
            '<ellipse cx="360" cy="270" rx="230" ry="145" fill="#C8B192"/>'
            '<ellipse cx="360" cy="258" rx="205" ry="122" fill="#E8D8B4"/>'
            '<ellipse cx="360" cy="252" rx="188" ry="108" fill="#D9B67C"/>'
            '<g fill="#B5574A"><ellipse cx="270" cy="220" rx="42" ry="16" transform="rotate(-18 270 220)"/>'
            '<ellipse cx="400" cy="205" rx="44" ry="16" transform="rotate(14 400 205)"/>'
            '<ellipse cx="335" cy="290" rx="40" ry="15" transform="rotate(-8 335 290)"/>'
            '<ellipse cx="455" cy="278" rx="36" ry="14" transform="rotate(22 455 278)"/></g>'
            '<g fill="#F2E6C8"><circle cx="240" cy="280" r="18"/><circle cx="455" cy="215" r="18"/><circle cx="370" cy="320" r="17"/></g>'
            '<path d="M120 170 q40 -30 80 0 M520 150 q40 -30 80 0" fill="none" stroke="#FFFFFF" stroke-width="6" opacity=".7"/>'
        ),
        "ferry": (
            f'<rect x="0" y="280" width="720" height="200" fill="{land}"/>'
            '<circle cx="580" cy="150" r="58" fill="#EAB773"/>'
            '<path d="M140 300 L580 300 L540 350 L180 350 Z" fill="#F1EADB" stroke="#8B6A45" stroke-width="4"/>'
            '<rect x="250" y="250" width="160" height="50" fill="#F1EADB" stroke="#8B6A45" stroke-width="4"/>'
            '<g fill="#8FB6C9"><rect x="270" y="265" width="28" height="20"/><rect x="315" y="265" width="28" height="20"/>'
            '<rect x="360" y="265" width="28" height="20"/></g>'
            '<rect x="320" y="210" width="8" height="42" fill="#8B6A45"/>'
            '<path d="M0 370 Q180 350 360 370 T720 365" fill="none" stroke="#FFFFFF" stroke-width="4" opacity=".6"/>'
        ),
        "night": (
            '<rect x="0" y="0" width="720" height="480" fill="#26313B"/>'
            '<g fill="#E9DFC7" opacity=".8"><circle cx="90" cy="70" r="3"/><circle cx="180" cy="110" r="2"/>'
            '<circle cx="300" cy="60" r="3"/><circle cx="470" cy="90" r="2"/><circle cx="620" cy="60" r="3"/></g>'
            '<rect x="0" y="310" width="720" height="170" fill="#3A4A50"/>'
            '<path d="M60 270 L660 270" stroke="#C8764A" stroke-width="9"/>'
            '<g fill="#C8764A"><path d="M170 230 h80 l-10 40 h-60 z"/><path d="M350 220 h90 l-12 50 h-66 z"/>'
            '<path d="M520 235 h70 l-8 35 h-54 z"/></g>'
            '<g fill="#F6D98A" opacity=".9"><path d="M210 225 L150 60 L270 60 Z"/><path d="M395 215 L320 40 L470 40 Z"/>'
            '<path d="M555 230 L510 80 L600 80 Z"/></g>'
            '<path d="M0 330 Q180 318 360 330 T720 326" fill="none" stroke="#F6D98A" stroke-width="3" opacity=".5"/>'
        ),
    }[kind]
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="480" viewBox="0 0 720 480" role="img">'
        f'<rect width="720" height="480" fill="{sky}"/>{body}'
        '<rect x="0" y="400" width="720" height="80" fill="#FCFBF7" opacity=".95"/>'
        f'<text x="28" y="438" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="27" font-weight="700" fill="{ink}">'
        f'{title}</text>'
        f'<text x="28" y="466" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="15" fill="#5C594E">'
        f'{sub}</text>'
        '<text x="692" y="440" text-anchor="end" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#8A8677">'
        '手绘示意 · 非实景</text></svg>'
    )
    return (
        '<figure><img src="data:image/svg+xml;base64,' + b64(svg) + '" alt="' +
        title + '（手绘示意）"><figcaption>' + title + '（示意）</figcaption></figure>'
    )


def photos(a, b):
    return '<div class="photos">' + a + b + '</div>'


def route(nodes, caption):
    """逐日动线示意，非等比；节点按真实先后顺序排。"""
    n = len(nodes)
    w = 680
    step = (w - 80) / max(1, n - 1)
    pts = []
    for i, nd in enumerate(nodes):
        x = 40 + i * step
        pts.append(
            f'<circle cx="{x:.0f}" cy="76" r="9" fill="#2F5D43"/>'
            f'<text x="{x:.0f}" y="112" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" '
            f'font-size="14" fill="#1C1B17">{nd}</text>'
        )
    line = f'<path d="M40 76 L{w-40} 76" fill="none" stroke="#2F5D43" stroke-width="2" stroke-dasharray="6 5"/>'
    return (
        '<div class="card" style="margin-top:14px"><div class="eyebrow">动线核对 · 示意非等比</div>'
        f'<svg class="route-svg" viewBox="0 0 {w} 140" width="100%" role="img" style="max-width:100%">'
        + line + ''.join(pts) + '</svg>'
        f'<div style="font-size:.75rem;color:#8A8677;margin-top:6px">{caption}；实际以导航为准</div></div>'
    )


P = {
    "d1": photos(
        fig("潮州广济桥", "十八梭船廿四洲 · 冬令时 16:30 清场", "bridge", "green"),
        fig("牌坊街与开元寺", "古城全程步行，石板路多", "arch", "amber")),
    "d2": photos(
        fig("南澳大桥与灯塔", "进岛收双程通行费 · 桥上限速 60", "lighthouse", "blue"),
        fig("青澳湾", "11 月不下海，只散步踩沙", "bay", "blue")),
    "d3": photos(
        fig("汕头小公园骑楼", "雨天最舒服的一段：有遮蔽", "arcade", "amber"),
        fig("潮汕牛肉火锅", "现切现涮 · 沙茶酱是灵魂", "hotpot", "green")),
    "d4": photos(
        fig("广场轮渡与海滨路", "一块钱的日落机位（天气允许时）", "ferry", "blue"),
        fig("广济桥灯光秀", "周二 20:00 一场 · 免费", "night", "night")),
}

CONTENT = r'''
<section id="overview">
  <div class="eyebrow">总览 · 行程速览</div>
  <h1>潮汕 4 天 · 一家三口（高铁往返 + 落地自驾）</h1>
  <p class="lead">深圳 → 潮州古城 → 汕头市区 / 南澳岛 → 深圳｜2026-11-17（周二）—11-20（周五），4 天 3 晚｜2 位成人 + 1 名小学生（7—12 岁）。</p>
  <p class="lead">地理归属：日常说的「潮汕」是潮州、汕头、揭阳三市的合称，不是一个市。本册只走 <b>潮州湘桥区古城</b>、<b>汕头金平／龙湖区</b> 与 <b>汕头下辖的南澳县（海岛县）</b>；揭阳、凤凰山、龙湖古寨都不排，理由见「备选」。</p>
  <div class="warn-line">⚠️ 出发前一晚（11/16）必须复核逐日预报：潮州气象台与墨迹对 11/18 晴雨有分歧，但两源都指向 <b>11/19 起明显降温</b>。海岛只排 11/18，后面两天留给骑楼、古城和吃——雨天不受影响的部分。若 11/18 确认中雨以上或 6 级以上大风，直接启动当天 Plan B，不硬上岛。</div>
  <div class="weather">
    <div class="wday"><div class="d">11/17 周二</div><div class="w">多云</div><div class="t">26 / 20℃</div></div>
    <div class="wday"><div class="d">11/18 周三</div><div class="w">晴雨有分歧</div><div class="t">24 / 17℃</div></div>
    <div class="wday"><div class="d">11/19 周四</div><div class="w">降温</div><div class="t">20 / 14℃</div></div>
    <div class="wday"><div class="d">11/20 周五</div><div class="w">偏冷</div><div class="t">15 / 12℃</div></div>
  </div>
  <p style="font-size:.76rem;color:#8A8677;margin-top:8px">天气来源：潮州市气象局 2026-11-14 15:30 更新（11/17 多云 26/20、11/18 多云 24/17、11/19 多云 20/14）；墨迹天气汕头逐日（11/14 查：11/17 少云 25/17、11/18 阴转阵雨 22/17、11/19 阴转阵雨 17/14、11/20 阵雨转少云 15/12）。两源口径不一致，已在正文按「共识＝11/19 起降温」处理，具体以出发前一晚为准。</p>
  <div class="card" id="prepCard">
    <div class="eyebrow">出发前 · 倒排行动清单</div>
    <h2>这几件不做会出事</h2>
    <ul class="check">
      <li class="hot"><input type="checkbox" id="c1"><div class="ct"><b>🚨 现在就买高铁票。</b>11/17 去程（深圳北 → <b>潮汕站</b>）、11/20 回程（<b>汕头站</b> → 深圳北）。车次与票价【未核实】——12306 官方余票接口两次访问均返回错误页，本册不编车次号；请在 12306 App 按下方「路程」给的时段窗口锁定，买完把时刻回填到逐日卡。</div></li>
      <li class="hot"><input type="checkbox" id="c2"><div class="ct"><b>🚨 一嗨下单前确认「异地还车费」。</b>潮汕高铁站店取、汕头高铁站店还正好顺着动线，但异地费口径【未核实】，以 App 下单页总价为准。若异地费明显高于 150 元，改走「省钱备选」：只在汕头站取还、租 D2 一天。</div></li>
      <li><input type="checkbox" id="c3"><div class="ct"><b>T-1（11/16 晚）天气终判。</b>看 11/18 逐时段预报与海上大风预警；中雨以上／6 级以上阵风＝南澳改室内，别赌。</div></li>
      <li><input type="checkbox" id="c4"><div class="ct"><b>广济桥上桥票：</b>「一票潮州」小程序提前买，11/1—1/31 冬令时工作日 10:00—16:30（16:00 停止上桥）。灯光秀免费、免预约。</div></li>
      <li><input type="checkbox" id="c5"><div class="ct"><b>南澳入岛预约：</b>周末／节假日走「南澳畅行」小程序；11/18 是周三，工作日通常无需预约，出发前在小程序确认当日口径即可。</div></li>
      <li><input type="checkbox" id="c6"><div class="ct"><b>保留高铁票根。</b>微信／云闪付搜「一票游广东」小程序上传抵达票根，可领「食在汕头」满减券（活动页显示至 2026-12-31）；潮州 9/9—10/8 那批票根券已结束，别按旧攻略找。</div></li>
      <li><input type="checkbox" id="c7"><div class="ct"><b>订房问三样：</b>有没有免费停车位、家庭房／双床能否加床、能不能免费取消（11/19 天气有变数，别锁不可退的房）。</div></li>
      <li><input type="checkbox" id="c8"><div class="ct"><b>装备：</b>薄防风外套×3（11/20 只有 12℃、海岛海风更冷）、折叠伞、防滑运动鞋、常用药（蒙脱石散、藿香正气、创可贴）、孩子学生证（广济桥半价）、少量现金（老店／停车）。11 月不下海，泳衣别带。</div></li>
    </ul>
  </div>
  <div class="card">
    <div class="eyebrow">这一趟的关键判断</div>
    <h2>为什么把海岛放第二天、为什么改成自驾</h2>
    <p style="font-size:.9rem;color:#5C594E">11/19 起降温、11/18 预报有分歧，所以南澳只能排前段；D3／D4 给骑楼、古城和美食，下雨也能照走。原骨架里写的「青澳湾日落」已收回：<b>日落 17:26（sunrise-sunset API 实查），看完再摸黑开 1 小时环岛路回汕头，带娃不安全</b>。主线改为 16:30 前离岛，日落改在市区广场轮渡看。</p>
    <p style="font-size:.9rem;color:#5C594E;margin-top:10px">你说可以在一嗨租车，这条成立，而且比包车划算：<b>潮汕高铁站店、汕头高铁站店都是站内取还</b>（一嗨官网门店页：潮汕站地面停车场 B 区，08:00—23:00；汕头站 B2 层，08:00—23:00），取还点正好压在「潮州进、汕头出」的动线上，不折返。真痛点是南澳环岛 70 km、景点散、11 月海风大且可能下雨，带娃等公交或骑电动车都不合适。代价是司机要开环岛弯多路、潮州古城和小公园两天车基本闲置（还得付停车费），以及异地还车费这个未核项。不做的代价：包车一天约 500—700 元＋其余打车 300—400 元，省两三百块但转场不自由、行李得搬。<b>结论：值得，主案按全程自驾；不想开或异地费偏高，就切「省钱备选」。</b></p>
  </div>
  ''' + route(["深圳北", "潮汕站", "潮州古城", "南澳岛", "汕头市区", "汕头站"], "总览动线：潮州进、汕头出，不走回头路") + r'''
</section>

<section id="drive">
  <div class="eyebrow">每段开多久</div>
  <h2>行 · 路程与停车</h2>
  <p class="lead">高铁往返 + 落地自驾。<b>潮汕站 ≠ 汕头站</b>：潮汕站在潮州潮安沙溪镇，到潮州古城约 30 分钟车程；汕头站在汕头市区，去小公园和南澳顺路。买错站＝白跑 40 分钟。</p>
  <table class="tb" style="table-layout:fixed"><colgroup><col style="width:26%"><col style="width:14%"><col style="width:18%"><col style="width:42%"></colgroup>
    <thead><tr><th>路段</th><th>里程</th><th>正常耗时</th><th>说明</th></tr></thead>
    <tbody>
      <tr><td><b>深圳北 → 潮汕站</b></td><td>约 300 km</td><td>2—2.5 h</td><td>高铁直达，班次密集；建议 09:30—10:30 发、12:00—13:00 到。<b>车次号／票价【未核实】</b>，12306 App 锁定后回填</td></tr>
      <tr><td><b>潮汕站 → 潮州古城</b></td><td>约 20 km</td><td>30 min</td><td>出站左转 B 区停车场取车 → 走潮汕路、南堤路进城；车停古城外围</td></tr>
      <tr><td><b>潮州古城 → 汕头市区</b></td><td>约 45 km</td><td>50—60 min</td><td>潮汕路／汕汾路方向，D2 早上出发</td></tr>
      <tr><td><b>汕头市区 → 南澳长山尾</b></td><td>约 35 km</td><td>50—60 min</td><td>南澳大桥约 9 km，全程限速 60、区间测速；桥上禁停车拍照</td></tr>
      <tr><td><b>南澳环岛（西线 → 青澳湾）</b></td><td>约 70 km</td><td>3—4 h（含停留）</td><td>弯多、临海，11 月海风大；带娃别骑电动车，别摸黑赶路</td></tr>
      <tr><td><b>汕头市区 → 汕头站</b></td><td>约 10 km</td><td>20 min</td><td>还车 + 返程，预留 1 小时缓冲</td></tr>
      <tr><td><b>汕头站 → 深圳北</b></td><td>约 300 km</td><td>2—2.5 h</td><td>建议 14:00—16:00 之间发车；<b>车次号／票价【未核实】</b></td></tr>
    </tbody>
  </table>
  <div class="card" style="margin-top:16px">
    <div class="eyebrow">一嗨租车 · 落地自驾</div>
    <h2>取还点与三种走法对照</h2>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:22%"><col style="width:30%"></colgroup>
      <thead><tr><th>方案</th><th>怎么用</th><th>大致花费（4 天）</th><th>适合</th></tr></thead>
      <tbody>
        <tr><td><b>主案 · 全程自驾</b></td><td>11/17 潮汕高铁站店取 → 11/20 汕头高铁站店还，4 天</td><td>租金约 ¥800—1100 + 油 ¥250 + 过桥 ¥96 + 停车 ¥80—150；异地还车费【未核实】</td><td>带娃行李不搬、雨天有车躲、南澳随停随走</td></tr>
        <tr><td><b>省钱备选</b></td><td>只在汕头站取还，租 D2 一天跑南澳；D1 潮汕站→古城打车、D1 晚转汕头打车</td><td>约 ¥300—500（单日租金 + 油 + 过桥 + 停车）</td><td>异地还车费过高，或不想在古城找车位</td></tr>
        <tr><td><b>不自驾</b></td><td>D2 包车一天上岛，其余打车／城际</td><td>约 ¥800—1100（包车 500—700 + 打车 300—400）</td><td>司机想歇、或 11/18 天气转差要临时改线</td></tr>
      </tbody>
    </table>
    <p style="font-size:.8rem;color:#8A8677;margin-top:10px">租金与包车价为公开攻略区间【估算】，一嗨实时价、车型、保险与异地费一律以 App 下单页为准；过桥费为 9 座及以下小客车 <b>96 元／往返</b>（进岛一次收双程、出岛不收，ETC 约 91.2 元；2026 年攻略口径）。</p>
  </div>
  <div class="card">
    <div class="eyebrow">🅿️ 逐日停车</div>
    <h2>车停哪、要不要换乘</h2>
    <ul class="check">
      <li><input type="checkbox" id="p1"><div class="ct"><b>D1 潮州古城：</b>车停北关停车场或古城外围停车场，古城内石板路 + 单行，全程步行。节假日古城限行需提前预约车辆，工作日以现场标识为准。收费【未核实】，以现场公示为准。</div></li>
      <li><input type="checkbox" id="p2"><div class="ct"><b>D2 南澳岛：</b>长山尾灯塔、青澳湾、总兵府均有停车点，景区停车约 ¥10—20／次；南澳大桥桥面严禁停车。黄花山森林公园如需上山，另查现场接驳口径。</div></li>
      <li><input type="checkbox" id="p3"><div class="ct"><b>D3 汕头小公园：</b>老城路窄、车位紧，建议车停酒店，步行或打车去骑楼区；别把车开进小公园的巷子里找位。</div></li>
      <li><input type="checkbox" id="p4"><div class="ct"><b>D4 还车：</b>汕头高铁站店在 B2 层（珠津南路 36 号），08:00—23:00；还车留 40 分钟验车，别压着发车时间到。</div></li>
    </ul>
    <p style="font-size:.82rem;color:#5C594E;margin-top:8px">支付：高速／过桥走 ETC 或微信、支付宝；古城小店、部分停车点备少量现金。堵车提示：南澳大桥 9—16 点为进岛高峰，11/18 是工作日，压力比周末小；出岛建议 16:30 前。</p>
  </div>
</section>

<section id="day1">
  <div class="day">
    <div class="day-head"><span class="day-idx">DAY 1 · 11/17 周二</span><h3>潮州古城 · 上桥、逛街、看灯光秀</h3><span class="today-badge">今天</span></div>
    <div class="note-row"><span class="ic">🧭</span><div><b>今日速览：</b>上午＝高铁到潮汕站、取车进城；下午＝开元寺、牌坊街、广济桥上桥；傍晚＝西马路小吃 + 20:00 广济桥灯光秀。</div></div>
    ''' + P["d1"] + r'''
    <div class="slot"><div class="slot-time">09:30</div><div class="slot-body"><b>早餐</b> · 深圳北站或车上解决，给孩子垫饱，别指望到站再找吃的。</div></div>
    <div class="slot"><div class="slot-time">10:00</div><div class="slot-body"><b>高铁 深圳北 → 潮汕站</b>（具体车次以 12306 锁定为准，建议 12:00—13:00 抵达）。出站左转 B 区停车场，一嗨潮汕高铁站店取车。</div></div>
    <div class="slot"><div class="slot-time">13:00</div><div class="slot-body"><b>午餐</b> · 进城先吃：<b>潮镇老尾牛杂粿条</b>（环城西路 107 号，07:30—18:30）或 <b>吴进平小食店</b>（西马路 306 号，10:00 至卖完）。一家三口点粿条汤 + 春饼 + 竹笋粿，别一次点太多，下午还要扫街。</div></div>
    <div class="slot"><div class="slot-time">14:00</div><div class="slot-body"><b>开元寺 → 牌坊街 → 甲第巷</b>：免费，全程步行。开元寺红墙、22 座明清石牌坊、南洋骑楼连成一条线，孩子看木雕和石坊比听讲解更有感觉。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 牌坊街：0.5x 广角蹲低，从街心往牌坊序列拍，人少时把孩子放在画面下三分之一。</div>
    <div class="slot"><div class="slot-time">15:15</div><div class="slot-body"><b>广济桥上桥</b>（门票 ¥20／学生 ¥10／1.2 m 以下免，「一票潮州」小程序）。冬令时工作日 10:00—16:30，<b>16:00 停止上桥</b>，别拖到傍晚。看「十八梭船廿四洲」的启闭式结构，走一趟约 40 分钟。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 广济楼城楼侧、下水门楼一带的桥侧面，下午顺光；手机开 2x 把桥亭和韩江压一起。</div>
    <div class="slot"><div class="slot-time">16:30</div><div class="slot-body"><b>西马路扫街</b>：咸水粿（开元上西平路口）、十八曲老尾鱼饺（西马路口对面）、胡荣泉鸭母捻与春卷（太平路）、甘草水果。主街溢价高，往巷子里走。</div></div>
    <div class="slot"><div class="slot-time">18:00</div><div class="slot-body"><b>晚餐</b> · <b>乌记明卤鹅（西马路 71—73 号，10:30—22:00）</b>：卤鹅拼盘 + 蚝烙 + 虾蟹砂锅粥，一家三口够。备选 <b>官塘兄弟牛肉火锅（市区店）</b>，孩子更认火锅。（更多选择在美食清单）</div></div>
    <div class="slot"><div class="slot-time">19:45</div><div class="slot-body"><b>广济桥灯光秀</b>：周二 20:00 一场、约 10 分钟，免费免预约；提前 20 分钟到广济楼—下水门楼一侧的江边占位。看完步行回酒店，属正常傍晚动线，不算熬夜。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 夜景模式 3 秒、手肘夹紧靠栏杆；桥体亮灯那一下连拍，别开闪光灯。</div>
    <div class="note-row"><span class="ic">🚇</span><div><b>今日交通：</b>高铁 + 取车后约 20 km 进城；古城内全程步行。<b>🅿️ 停车：</b>北关停车场／古城外围，进古城不开车。</div></div>
    <div class="note-row"><span class="ic">💡</span><div><b>你知道吗：</b>广济桥被桥梁专家茅以升称作「世界上最早的启闭式桥梁」——中间那段浮桥由 18 只梭船连成，每天定时拆合，所以潮州人管它叫「过河拆桥」，是字面意思。</div></div>
    <div class="warn-line"><b>🛟 当天 Plan B：</b>列车晚点超过 1 小时 → 砍掉上桥，只逛牌坊街 + 西马路，把广济桥上桥挪到 D4 上午不现实（已转场），所以优先保灯光秀；下雨 → 开元寺、广济楼、载阳茶馆喝工夫茶，灯光秀若遇极端天气取消就早回酒店。</div>
  </div>
  ''' + route(["深圳北", "潮汕站", "古城外围停车", "开元寺/牌坊街", "广济桥", "灯光秀/酒店"], "D1 单集群：古城内一条线走完，不横穿") + r'''
</section>

<section id="day2">
  <div class="day">
    <div class="day-head"><span class="day-idx">DAY 2 · 11/18 周三</span><h3>南澳岛 · 灯塔、环岛西线、青澳湾</h3><span class="today-badge">今天</span></div>
    <div class="note-row"><span class="ic">🧭</span><div><b>今日速览：</b>上午＝潮州转汕头、上岛；下午＝长山尾灯塔 → 钱澳湾 → 三囱崖灯塔 → 青澳湾；傍晚＝16:30 前离岛，回汕头市区吃饭。<b>不追海岛日落，不摸黑开环岛路。</b></div></div>
    ''' + P["d2"] + r'''
    <div class="slot"><div class="slot-time">08:30</div><div class="slot-body"><b>早餐</b> · 酒店含早就吃酒店；不含早去 <b>一家人肠粉</b>（太平路 159 号）或 <b>阿臣肠粉</b>（开元路义安路 14 号，07:00—13:00）。潮州肠粉淋花生酱，跟广式不是一回事。</div></div>
    <div class="slot"><div class="slot-time">09:30</div><div class="slot-body"><b>退房上车，潮州 → 汕头 → 南澳大桥</b>，约 1.5—2 小时。经过汕头市区可先进 <b>小吴肠粉</b>（龙眼南路椰园 4 幢 101 号）补一份，或直接上岛。</div></div>
    <div class="slot"><div class="slot-time">11:00</div><div class="slot-body"><b>进岛</b>：南澳大桥收费站（长山尾侧）一次收往返 ¥96，出岛不再收。桥上限速 60、禁停车拍照。若「南澳畅行」显示当日需预约，提前 7 天内约好时段。</div></div>
    <div class="slot"><div class="slot-time">11:30</div><div class="slot-body"><b>午餐</b> · 后宅镇本地排档（明码标价的那种）：紫菜炒饭、海胆蒸蛋、白灼虾、鱼丸汤。11 月是南澳头水紫菜采收季，秋冬海鲜也肥。<b>避开青澳湾网红大排档</b>，价格虚高。</div></div>
    <div class="slot"><div class="slot-time">12:30</div><div class="slot-body"><b>长山尾灯塔 → 钱澳湾灯塔 → 三囱崖灯塔</b>：环岛西线，红白塔身配跨海大桥，随停随拍，观景点基本免费。孩子跑得开，每个点停 20—30 分钟就够。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 长山尾灯塔：0.5x 广角把大桥一起收进去；海风大，手机贴身别举太高。</div>
    <div class="slot"><div class="slot-time">14:30</div><div class="slot-body"><b>青澳湾 + 北回归线标志塔「自然之门」</b>：沙细人少，散步踩沙、捡贝壳，<b>11 月水温低不下海游泳</b>。精力够可顺路看风车山观景台；带孩子不强求登高。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 青澳湾：下午侧光，蹲低用沙滩纹路当前景；北回归线塔用 2x 压掉杂乱背景。</div>
    <div class="slot"><div class="slot-time">16:30</div><div class="slot-body"><b>离岛回汕头市区</b>。日落 17:26（sunrise-sunset API 实查），这一小时正好用在回程上，不摸黑走环岛路。入住汕头市区酒店，车停酒店。</div></div>
    <div class="slot"><div class="slot-time">18:30</div><div class="slot-body"><b>晚餐</b> · <b>杏花吴记牛肉火锅</b>（金砂西路新荷花园 A 栋 1 层，09:30—21:30，人均约 ¥104）或 <b>春梅里鹅肉店</b>（中山路 71 号）。现切吊龙、五花趾、手打牛肉丸，最后用汤底烫粿条收尾。（更多选择在美食清单）</div></div>
    <div class="note-row"><span class="ic">🚇</span><div><b>今日交通：</b>全天自驾约 150—180 km，潮州→汕头→南澳→汕头，司机约 4 小时。<b>🅿️ 停车：</b>长山尾／青澳湾景区停车 ¥10—20／次，桥面严禁停车。</div></div>
    <div class="note-row"><span class="ic">💡</span><div><b>你知道吗：</b>南澳大桥的过桥费是「进岛一次收双程」——出岛直接放行。所以别在出岛口再找收费站，也别被网上「单程 48 元」的说法绕晕，小车实际一次付 96 元。</div></div>
    <div class="warn-line"><b>🛟 当天 Plan B：</b>11/18 确认中雨以上／6 级以上阵风／大桥临时管制 → <b>整段南澳取消</b>，改汕头市区室内线：小公园开埠文化陈列馆 + 汕头市博物馆 + 龙眼南路美食 + 商场，车也不必上桥。若只是零星小雨，保留西线灯塔、砍掉青澳湾和风车山，提前回城。</div>
  </div>
  ''' + route(["潮州古城", "汕头市区", "长山尾灯塔", "钱澳湾/三囱崖", "青澳湾", "汕头市区"], "D2 单向环岛：西线进、东线出，16:30 前离岛") + r'''
</section>

<section id="day3">
  <div class="day">
    <div class="day-head"><span class="day-idx">DAY 3 · 11/19 周四</span><h3>汕头市区 · 骑楼、轮渡、慢吃一天</h3><span class="today-badge">今天</span></div>
    <div class="note-row"><span class="ic">🧭</span><div><b>今日速览：</b>上午＝小公园骑楼 + 开埠陈列馆（室内）；下午＝龙眼南路扫街、广场轮渡；晚上＝夜糜打冷或砂锅粥。降温 + 阵雨的一天，全程有遮蔽、不赶路。</div></div>
    ''' + P["d3"] + r'''
    <div class="slot"><div class="slot-time">09:00</div><div class="slot-body"><b>早餐</b> · <b>小吴肠粉</b>（龙眼南路椰园 4 幢 101 号，08:00—13:30）或 <b>海记猪血汤</b>（龙华街凤园二栋 106 号，只做中午前）。孩子不爱内脏就选全拼肠粉。</div></div>
    <div class="slot"><div class="slot-time">10:00</div><div class="slot-body"><b>小公园开埠区</b>：中山纪念亭为中心，放射状骑楼街。骑楼有连廊，下雨也能逛。顺路进 <b>汕头开埠文化陈列馆</b>（免费，室内，具体开放以现场公示为准）和老妈宫戏台。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 中山纪念亭：站亭子对角，0.5x 仰拍把骑楼弧线收进来；雨天地面的反光别躲，是这天的加分项。</div>
    <div class="slot"><div class="slot-time">11:30</div><div class="slot-body"><b>午餐</b> · <b>爱西干面（国平路 1 号）</b> 干面 + 肉丸汤，或 <b>老妈宫粽球／小公园老牌粽球</b>（新关街 9—10 号）双烹粽球。这两样分量实在，留肚子给下午。</div></div>
    <div class="slot"><div class="slot-time">13:30</div><div class="slot-body"><b>回酒店休息 1 小时</b>。降温天带娃连走两天容易垮，这段午休是硬留的，不是「有空才休」。</div></div>
    <div class="slot"><div class="slot-time">15:00</div><div class="slot-body"><b>龙眼南路扫街</b>：福铭蚝烙（龙眼路 62-1 号）、广场老牌豆花甜汤（公园路汇涛花园 1 楼）、亚强果汁冰（中山路 52 号）、杨记杏仁茶（龙眼路 62 号）。甜汤偏甜，可让店家少糖。</div></div>
    <div class="slot"><div class="slot-time">16:40</div><div class="slot-body"><b>广场轮渡</b>：¥1 坐一趟看海湾，天气好正好赶上日落（约 17:25）。风大或下雨就改去附近商场／茶馆，别在码头硬等。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 轮渡上隔着玻璃拍对岸，镜头贴玻璃消反光；开「实况」后期转长曝光，水面更平。</div>
    <div class="slot"><div class="slot-time">18:30</div><div class="slot-body"><b>晚餐</b> · <b>适口餐厅砂锅粥</b>（公信路 29 号之一，螃蟹鲜虾粥 + 菜脯煎蛋）或 <b>富苑饮食</b>（朝阳庄北区 12 栋，打冷自选）。带娃建议砂锅粥，生腌只让大人浅尝、先吃半碗白粥打底。（更多选择在美食清单）</div></div>
    <div class="note-row"><span class="ic">🚇</span><div><b>今日交通：</b>车停酒店，老城区步行 + 打车；小公园巷子窄，别开车进去。<b>🅿️ 停车：</b>酒店车位，确认是否免费。</div></div>
    <div class="note-row"><span class="ic">💡</span><div><b>你知道吗：</b>汕头话把大排档那套「白粥配几十种冷盘热菜」叫「夜糜／打冷」，白粥不是主角，旁边那一长排鱼饭、生腌、卤水才是。点菜方式是站着看菜指菜，不翻菜单。</div></div>
    <div class="warn-line"><b>🛟 当天 Plan B：</b>雨大 → 全程室内：开埠文化陈列馆 + 汕头市博物馆 + 万象城，扫街挪到酒店附近；孩子累了 → 砍掉轮渡，午休延长，晚餐就近选酒店周边砂锅粥。</div>
  </div>
  ''' + route(["酒店", "小公园骑楼", "开埠陈列馆", "午休", "龙眼南路", "广场轮渡", "晚餐"], "D3 单集群：金平老城 + 龙眼南路，不跨区横穿") + r'''
</section>

<section id="day4">
  <div class="day">
    <div class="day-head"><span class="day-idx">DAY 4 · 11/20 周五</span><h3>早茶收尾 · 还车返深</h3><span class="today-badge">今天</span></div>
    <div class="note-row"><span class="ic">🧭</span><div><b>今日速览：</b>上午＝潮式早茶 / 再补一顿牛肉火锅；中午＝退房；下午＝汕头站还车 + 高铁回深圳。全天最冷（15/12℃），不排户外。</div></div>
    ''' + P["d4"] + r'''
    <div class="slot"><div class="slot-time">09:00</div><div class="slot-body"><b>早餐</b> · <b>韩上楼</b>（凤洲西路凤凰洲公园内，07:30—20:30，广式早茶 + 潮州菜）或 <b>小吴肠粉</b> 二刷。行李先放车上／前台寄存。</div></div>
    <div class="slot"><div class="slot-time">10:30</div><div class="slot-body"><b>手信补给</b>：腐乳饼、绿豆饼去 <b>胡荣泉</b>（太平路）或 <b>权记饼食</b>（牌坊街，D1 已路过可当时买）；凤凰单丛、老香黄认市区老店，别在景区出口买礼盒。细目见「特产」。</div></div>
    <div style="font-size:.78rem;color:#8A8677;padding-left:110px">📷 位置：凤凰洲公园韩江边｜时段：09:30—10:30｜拍法：1x 平视把韩江与对岸收进画面，阴天别把 HDR 开过猛。</div>
    <div class="slot"><div class="slot-time">11:45</div><div class="slot-body"><b>午餐</b> · 最后一顿牛肉火锅：<b>八合里海记（八合里总店，黄岗路坪东 5 座 1 层，09:30—23:30，人均约 ¥90）</b> 或昨天没吃成的杏花吴记。吃完直接去车站方向，不折返。</div></div>
    <div class="slot"><div class="slot-time">13:30</div><div class="slot-body"><b>汕头站还车</b>：一嗨汕头高铁站店（B2 层，08:00—23:00），留 40 分钟验车、加油、结算。<b>异地还车费与超时费以下单页为准</b>。</div></div>
    <div class="slot"><div class="slot-time">14:30</div><div class="slot-body"><b>高铁 汕头站 → 深圳北</b>，建议 14:00—16:00 之间发车，约 2—2.5 小时，傍晚到家。<b>车次号／票价【未核实】</b>，出发当天早上在 12306 复核一次运行图。</div></div>
    <div class="slot"><div class="slot-time">17:30</div><div class="slot-body"><b>晚餐</b> · 到家自行解决；若车上饿了，备点 D1 买的腐乳饼 / D4 打包的粿品，别在车站买溢价礼盒。</div></div>
    <div class="note-row"><span class="ic">🚇</span><div><b>今日交通：</b>市区 → 汕头站约 10 km / 20 分钟，还车 + 候车预留 1 小时。<b>🅿️ 停车：</b>汕头站 B2 一嗨还车点，进站前先看清取车指引图。</div></div>
    <div class="note-row"><span class="ic">💡</span><div><b>你知道吗：</b>潮汕牛肉火锅讲究「屠宰到上桌 4 小时内」，所以本地名店中午和傍晚各有一波鲜肉到店；下午三四点去，常能赶上晚市第一波最好的部位。</div></div>
    <div class="warn-line"><b>🛟 当天 Plan B：</b>还车排队／验车超时 → 先退掉早茶，直奔车站；高铁晚点 → 汕头站周边商场候车，别改签成深夜车；孩子不舒服 → 砍掉手信补给，直接还车进站。</div>
  </div>
  ''' + route(["酒店", "早茶", "手信", "午餐", "汕头站还车", "深圳北"], "D4 车站方向收尾：最后一个点排在去车站的路上") + r'''
</section>

<section id="boost">
  <div class="eyebrow">可选 · 更从容</div>
  <h2>备选、加餐与特殊时段玩法</h2>
  <div class="card">
    <div class="eyebrow">没排进主线，但值得知道</div>
    <h2>取舍说明</h2>
    <p style="font-size:.9rem;color:#5C594E"><b>揭阳、凤凰山、龙湖古寨</b>都不排：4 天塞进第四个地方，等于每天换城，带娃必赶；南澳已经吃掉一整天的车程。想加，最少再加 1 天，且建议单独做「潮州 + 凤凰单丛茶山」一趟。<b>住岛看日出</b>也不排：那是 B 方案，要搬两次家，且 11/19 降温阵雨，日出大概率落空。</p>
  </div>
  <div class="card">
    <div class="eyebrow">⏰ 特殊时段玩法</div>
    <h2>错过就废的项目，都在这儿</h2>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:26%"><col style="width:34%"><col style="width:40%"></colgroup>
      <thead><tr><th>项目</th><th>时点与口径</th><th>怎么安排</th></tr></thead>
      <tbody>
        <tr><td><b>广济桥灯光秀</b></td><td>周一至周四 20:00 一场；周五六日 20:00 + 21:30，约 10 分钟，免费</td><td><b>主线 D1 已排</b>（11/17 周二场）。提前 20 分钟到广济楼—下水门楼一侧</td></tr>
        <tr><td><b>广济桥「过河拆桥」</b></td><td>冬令时工作日 16:30 清场，浮桥拆卸时点以现场公示为准</td><td>D1 上桥时顺带问工作人员，不单独为它改行程</td></tr>
        <tr><td><b>青澳湾海上日出</b></td><td>11/18 日出约 06:28（sunrise-sunset API 实查），需 05:30 起</td><td>归「🌅 早起包」：只有住岛才成立，本册 A 方案住市区，<b>不去</b>；想要就改 B 方案</td></tr>
        <tr><td><b>日落 / 蓝调</b></td><td>11/17 日落 17:28、11/18 南澳 17:26（API 实查）</td><td>D2 不追海岛日落（摸黑环岛不安全），改 D3 广场轮渡 / 海滨路，天气允许才去</td></tr>
        <tr><td><b>星空 / 银河</b></td><td>海岛光污染少，但需查月相；11/18 前后若满月则放弃</td><td>不进主线（需 22:00 后在外）。本册未查月相，标【未核实】，不硬排</td></tr>
        <tr><td><b>赶海</b></td><td>需退潮时刻，本册未查潮汐表【未核实】</td><td>D2 青澳湾只做踩沙捡贝壳，不承诺赶海；要玩先查当日潮汐</td></tr>
        <tr><td><b>夜糜宵夜</b></td><td>富苑 24h、长平老姿娘夜粥 24h</td><td>归「🌙 夜游包」：大人自愿，回酒店约 23:00；孩子按正常作息睡</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section id="ticket">
  <div class="eyebrow">进门花多少</div>
  <h2>门票与预约</h2>
  <table class="tb" style="table-layout:fixed"><colgroup><col style="width:26%"><col style="width:20%"><col style="width:16%"><col style="width:38%"></colgroup>
    <thead><tr><th>景点</th><th>全价</th><th>小孩</th><th>关键时间 / 口径</th></tr></thead>
    <tbody>
      <tr><td><b>广济桥（上桥）</b></td><td>¥20</td><td>学生 ¥10；1.2 m 以下免</td><td>「一票潮州」小程序预约购票；<b>11/1—1/31 冬令时</b>工作日 10:00—16:30（16:00 停止上桥），周末 9:00—17:30。查：2026-11-14 · 南方+／潮趣宝公众号</td></tr>
      <tr><td><b>广济桥联票</b></td><td>¥30 / ¥42 / ¥72</td><td>按景区口径</td><td>同程在售页：分别含 2／4／7 个景点（北阁佛灯修缮中）。带娃只上桥就买 ¥20 单票，别为凑点数买联票</td></tr>
      <tr><td><b>广济桥灯光秀</b></td><td>免费</td><td>免费</td><td>周二 20:00 一场；极端天气取消。免预约，看江边即可</td></tr>
      <tr><td><b>开元寺 / 牌坊街 / 广济楼外观</b></td><td>免费</td><td>免费</td><td>古城开放式街区，无预约；韩文公祠免费但需预约，本册未排</td></tr>
      <tr><td><b>南澳大桥通行</b></td><td>¥96／往返（小车）</td><td>—</td><td>进岛一次收双程，ETC 约 ¥91.2；法定节假日 7 座及以下免。周末／节假日「南澳畅行」小程序预约（最多提前 7 天）</td></tr>
      <tr><td><b>南澳环岛观景点</b></td><td>多数免费</td><td>免费</td><td>长山尾／钱澳湾／三囱崖灯塔、青澳湾、北回归线广场免费；停车 ¥10—20／次</td></tr>
      <tr><td><b>黄花山森林公园</b></td><td>¥20</td><td>以现场为准</td><td>08:30—17:30（去哪儿攻略口径）。本册未排上山，列作 D2 精力富余时的可选项</td></tr>
      <tr><td><b>总兵府 / 宋井</b></td><td>以现场公示为准</td><td>以现场为准</td><td>【未核实】官方渠道未查到稳定票价，现场看公示再决定进不进</td></tr>
    </tbody>
  </table>
  <p style="font-size:.8rem;color:#8A8677;margin-top:10px">🎫 票根优惠：微信／云闪付「一票游广东」小程序上传抵达高铁票根，可领「食在汕头」满 100 减 20 等满减券（活动页显示至 2026-12-31，权益以小程序实际为准）。潮州 2026 年「票根经济」消费券活动期为 9/9—10/8，<b>11 月已结束</b>。</p>
</section>

<section id="tips">
  <div class="eyebrow">真实场景 · 提前知道</div>
  <h2>提示与避雷</h2>
  <div class="tips">
    <div class="tip"><div><b>买票别买错站。</b>潮汕站在潮州潮安，汕头站在汕头市区，两站差约 40 分钟车程。去程要「潮汕站」，回程要「汕头站」，反过来走就是白绕一圈。</div></div>
    <div class="tip"><div><b>古城内别开车找车位。</b>牌坊街一带石板路 + 单行 + 节假日限行预约，车停北关或外围停车场，全程步行；高跟鞋和拉杆箱在石板路上都难受。</div></div>
    <div class="tip"><div><b>广济桥 16:00 就停止上桥。</b>冬令时（11 月起）比夏天早收 1 小时，按「下午两点半到桥」排，别照着暑期攻略 17:30 去。</div></div>
    <div class="tip"><div><b>牌坊街、小公园主街小吃溢价高。</b>往西马路、义安路、龙眼南路、居民区巷子里走，门头破但本地人排队的店更稳；看菜单明码标价再点。</div></div>
    <div class="tip"><div><b>南澳海鲜先问价再下单。</b>选后宅镇／云澳渔港明码标价的排档，避开青澳湾网红店；流动摊贩容易缺斤短两。孩子那份点熟食，别上生腌。</div></div>
    <div class="tip"><div><b>生腌别给孩子。</b>被叫「潮汕毒药」不是夸奖，肠胃弱的人浅尝都可能不舒服；大人要试，先吃半碗白粥打底，备蒙脱石散。</div></div>
    <div class="tip"><div><b>南澳大桥上不能停车拍照。</b>全长约 9 km、限速 60、区间测速全覆盖，压线／停车／上下客都抓拍；想拍桥去长山尾灯塔那边。</div></div>
    <div class="tip"><div><b>11 月别下海、别租电动车环岛。</b>水温偏低，海岛风大、环岛弯多，带娃骑电动车既冷又不安全；自驾或包车是这季的正确答案。</div></div>
    <div class="tip"><div><b>环比别摸黑。</b>11/18 日落约 17:26，看完再开 1 小时环岛夜路回市区不值；16:30 前离岛，日落留给市区轮渡。</div></div>
    <div class="tip"><div><b>降温那天别硬凑户外。</b>11/19—20 最低 12—14℃，加上海风体感更低；骑楼、陈列馆、茶馆、砂锅粥都是不依赖天气的选项。</div></div>
    <div class="tip"><div><b>租车下单页看总价，不看「每天起」。</b>租金之外还有基础保险、异地还车费、油费、过桥 ¥96、停车费；取车时拍一圈车身视频，还车留 40 分钟验车。</div></div>
    <div class="tip"><div><b>老店有脾气。</b>部分小食店只收现金、卖完收摊、只做午市前（海记猪血汤 13:30 收、西新玉记猪脚圈中午关门）。到店先看营业时段，别扑空了怪攻略。</div></div>
  </div>
  <div class="card">
    <div class="eyebrow">贴身提醒</div>
    <p style="font-size:.9rem;color:#5C594E">带娃三件：每天留一段午休（D3 已写进主线）、正餐别排长队名店（就近优先）、薄防风外套随身别放车上——11/20 只有 12℃，从酒店走到车站那段最冷。常用药放随身包，不放后备箱。</p>
  </div>
</section>

<section id="stay">
  <div class="eyebrow">住宿</div>
  <h2>住哪、怎么选</h2>
  <table class="tb" style="table-layout:fixed"><colgroup><col style="width:18%"><col style="width:30%"><col style="width:24%"><col style="width:28%"></colgroup>
    <thead><tr><th>晚</th><th>区域与理由</th><th>房型 / 含早</th><th>价档与取消</th></tr></thead>
    <tbody>
      <tr><td><b>11/17 潮州 1 晚</b></td><td>牌坊街／中山路一带，步行到开元寺、广济桥、灯光秀都在 15 分钟内；别订名字带「古城店」但离牌坊街很远的连锁</td><td>家庭房或双床 + 加床；优先含早（省得早上找店）；电梯房低楼层</td><td>11 月淡季，古城民宿家庭房约 ¥300—600／晚【估算，未实查实时价】；选可免费取消</td></tr>
      <tr><td><b>11/18—19 汕头 2 晚</b></td><td>二选一：小公园／金平老城（离骑楼、老字号近）或万象城／龙眼南路（新、停车方便、美食密）。<b>自驾优先后者</b>，老城巷子窄</td><td>双床房连住 2 晚不换店；问清免费车位</td><td>约 ¥300—550／晚【估算】；连住可问拆单比价，两晚拆两单有时更便宜</td></tr>
    </tbody>
  </table>
  <p style="font-size:.82rem;color:#5C594E;margin-top:10px">选房顺位：①位置顺着「潮州进、汕头出」的动线 ②预算 ③海景／特色只是加分项 ④D1 灯光秀机位（广济楼—下水门楼）距离 ≤1.5 km，才能先放包再赶上 20:00 那场。房价未逐家实查，下单前按日期在 OTA 比价；11/19 天气有变数，别锁不可退的房。</p>
</section>

<section id="cost">
  <div class="eyebrow">心里有数</div>
  <h2>预算（一家三口 · 4 天 3 晚）</h2>
  <div class="stats">
    <div class="stat"><div class="n">¥6,300—8,500</div><div class="l">主线合计（含高铁 / 租车 / 住宿 / 吃 / 门票）</div></div>
    <div class="stat"><div class="n">¥2,100—2,800</div><div class="l">人均（3 人分摊）</div></div>
    <div class="stat"><div class="n">弹性最大</div><div class="l">手信、海鲜、升级餐位</div></div>
  </div>
  <table class="tb" style="table-layout:fixed"><colgroup><col style="width:24%"><col style="width:22%"><col style="width:54%"></colgroup>
    <thead><tr><th>项</th><th>金额</th><th>口径与说明</th></tr></thead>
    <tbody>
      <tr><td><b>高铁往返</b></td><td>¥900—1,400</td><td>3 人 × 往返，二等座百元级；<b>票价【未核实】</b>，以 12306 实价为准（同日聚合页曾出现 ¥148 与 ¥85.5 两种口径，不采信）</td></tr>
      <tr><td><b>租车 4 天</b></td><td>¥800—1,100</td><td>经济／紧凑型租金 + 基础保险【估算】；异地还车费【未核实】，下单页为准</td></tr>
      <tr><td><b>油费</b></td><td>¥200—300</td><td>全程约 300 km，含南澳环岛</td></tr>
      <tr><td><b>过桥费</b></td><td>¥96</td><td>9 座及以下小车往返，ETC 约 ¥91.2（隐藏成本，别漏）</td></tr>
      <tr><td><b>停车费</b></td><td>¥80—150</td><td>古城外围 + 南澳景区 ¥10—20／次 + 酒店车位（自驾场景专项）</td></tr>
      <tr><td><b>住宿 3 晚</b></td><td>¥900—1,700</td><td>潮州 1 晚 + 汕头 2 晚，家庭房／双床，淡季区间【估算】</td></tr>
      <tr><td><b>餐饮</b></td><td>¥1,800—2,600</td><td>3 人 × 4 天，含 2 顿牛肉火锅（人均 ¥90—105）+ 小吃扫街 + 海鲜一顿；海鲜点多了是最大浮动口</td></tr>
      <tr><td><b>门票</b></td><td>¥60—100</td><td>广济桥 3 人（成人 ¥20 ×2 + 学生 ¥10）+ 可能的黄花山 ¥20／人；灯光秀与骑楼免费</td></tr>
      <tr><td><b>市内杂项</b></td><td>¥150—300</td><td>打车、轮渡、茶饮、行李寄存</td></tr>
      <tr><td><b>手信 / 伴手礼</b></td><td>¥300—800 <span class="tag dim">弹性最大</span></td><td>腐乳饼、单丛茶、紫菜、牛肉丸真空装；不买也完全成立</td></tr>
      <tr><td><b>旅行意外险</b></td><td>¥30—60</td><td>3 人 4 天短期险，建议买</td></tr>
    </tbody>
  </table>
  <p style="font-size:.82rem;color:#8A8677;margin-top:10px">合计口径：主选 + 已核实／估算项。标【未核实】的高铁票价与异地还车费未计入确定值，只按区间估算，出票后按实付替换。支付：微信／支付宝覆盖绝大多数场景，古城小店与部分停车点备 ¥100 现金即可。</p>
</section>

<section id="sos">
  <div class="eyebrow">应急</div>
  <h2>跨天兜底</h2>
  <div class="sos-grid">
    <div class="sos"><h4>🌧 暴雨 / 大风 / 封桥</h4><p>南澳整段取消，切 D3 的市区室内线提前一天走；大桥 9 级以上大风会分级管控，以现场公告为准，不赌不硬闯。潮州古城改开元寺 + 茶馆。</p></div>
    <div class="sos"><h4>🚄 错过车 / 车次变动</h4><p>高铁发车当天早上复核运行图；误车走 12306 改签，别买黄牛。去程晚点 >1h 就砍 D1 上桥，保灯光秀。</p></div>
    <div class="sos"><h4>🎫 约满 / 停演</h4><p>广济桥约满 → 江边看外观 + 灯光秀照常（免费）；灯光秀极端天气取消 → 早回酒店，不补拍。</p></div>
    <div class="sos"><h4>🤢 肠胃不适</h4><p>生腌、海鲜先停，改白粥 / 粿条汤；蒙脱石散、藿香正气随身。孩子发热就砍当天全部户外，酒店休息优先。</p></div>
    <div class="sos"><h4>🚗 车辆故障 / 违章</h4><p>一嗨 24h 道路救援走 App 报单；桥上故障开双闪、人员撤到护栏外、150 m 外放警示牌，别在桥上修车。</p></div>
    <div class="sos"><h4>📞 常用号码</h4><p>110 报警 / 120 急救 / 119 消防 / 12306 铁路 / 12315 消费投诉 / 一嗨客服见 App 订单页。</p></div>
  </div>
</section>

<section id="eat">
  <div class="eyebrow">照着吃就行</div>
  <h2>美食清单</h2>
  <p class="lead">按天分组，跟着动线走；每餐给主选 + 备选，别一顿吃太饱。人均多为公开攻略口径，未逐家实查的标【估算】，现场菜单为准。</p>
  <div class="card"><div class="eyebrow">第 1 天 · 潮州古城小吃与卤鹅</div>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:13%"><col style="width:17%"><col style="width:24%"><col style="width:28%"><col style="width:18%"></colgroup>
      <thead><tr><th>餐段</th><th>位置</th><th>店</th><th>点什么</th><th>人均</th></tr></thead>
      <tbody>
        <tr><td><b>午餐</b></td><td>环城西路</td><td>潮镇老尾牛杂粿条（107 号，07:30—18:30）</td><td>牛杂粿条、牛丸粿条</td><td>¥20—30【估算】</td></tr>
        <tr><td><b>午餐备选</b></td><td>西马路 306 号</td><td>吴进平小食店（10:00 至卖完）</td><td>春饼、竹笋粿、韭菜粿</td><td>¥15—25【估算】</td></tr>
        <tr><td><b>下午小吃</b></td><td>开元路 × 上西平路</td><td>开元上西平咸水粿（11:00—23:00）</td><td>咸水粿，菜脯是灵魂</td><td>¥11</td></tr>
        <tr><td><b>下午小吃</b></td><td>西马路口对面</td><td>十八曲老尾鱼饺店（07:30—24:00）</td><td>鱼饺／鱼面全家福</td><td>¥25【估算】</td></tr>
        <tr><td><b>晚餐</b></td><td>西马路 71—73 号</td><td>乌记明卤鹅（10:30—22:00）</td><td>卤鹅拼盘、蚝烙、虾蟹砂锅粥</td><td>¥60—90【估算】</td></tr>
        <tr><td><b>晚餐备选</b></td><td>官塘镇 / 市区</td><td>官塘兄弟牛肉火锅（总店 10:00—22:00）</td><td>吊龙、五花趾、手打牛肉丸</td><td>¥80—100【估算】</td></tr>
        <tr><td><b>甜汤</b></td><td>太平路 183 号</td><td>胡荣泉（10:00—19:00）</td><td>鸭母捻、春卷</td><td>¥10—15</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card"><div class="eyebrow">第 2 天 · 海岛紫菜与汕头牛肉</div>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:13%"><col style="width:17%"><col style="width:24%"><col style="width:28%"><col style="width:18%"></colgroup>
      <thead><tr><th>餐段</th><th>位置</th><th>店</th><th>点什么</th><th>人均</th></tr></thead>
      <tbody>
        <tr><td><b>早餐</b></td><td>太平路 159 号</td><td>一家人肠粉</td><td>花生酱肠粉</td><td>¥10—15【估算】</td></tr>
        <tr><td><b>早餐备选</b></td><td>开元路义安路 14 号</td><td>阿臣肠粉（07:00—13:00）</td><td>芝麻酱肠粉</td><td>¥10—15【估算】</td></tr>
        <tr><td><b>午餐</b></td><td>南澳后宅镇</td><td>后宅镇本地排档（明码标价，现场挑）</td><td>紫菜炒饭、海胆蒸蛋、白灼虾、鱼丸汤</td><td>¥60—100【估算】</td></tr>
        <tr><td><b>午餐备选</b></td><td>云澳渔港</td><td>渔港周边排档</td><td>清蒸石斑、蒜蓉生蚝、龙须菜鱼丸汤</td><td>¥60—100【估算】</td></tr>
        <tr><td><b>晚餐</b></td><td>金砂西路新荷花园 A 栋</td><td>杏花吴记牛肉火锅（09:30—21:30）</td><td>吊龙、雪花、五花趾、胸口油、粿条收尾</td><td>¥104</td></tr>
        <tr><td><b>晚餐备选</b></td><td>中山路 71 号</td><td>春梅里鹅肉店（08:00—13:00 / 15:00—19:00）</td><td>鹅粉肝、卤鹅三拼</td><td>¥60【估算】</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card"><div class="eyebrow">第 3 天 · 老城粿品与夜糜</div>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:13%"><col style="width:17%"><col style="width:24%"><col style="width:28%"><col style="width:18%"></colgroup>
      <thead><tr><th>餐段</th><th>位置</th><th>店</th><th>点什么</th><th>人均</th></tr></thead>
      <tbody>
        <tr><td><b>早餐</b></td><td>龙眼南路椰园 4 幢 101</td><td>小吴肠粉（08:00—13:30 / 17:00—20:00）</td><td>猪肉海鲜蛋肠粉、全拼</td><td>¥15</td></tr>
        <tr><td><b>早餐备选</b></td><td>龙华街凤园二栋 106</td><td>海记猪血汤（做到 13:30）</td><td>招牌猪血汤 + 煎饺</td><td>¥20【估算】</td></tr>
        <tr><td><b>午餐</b></td><td>国平路 1 号</td><td>爱西干面（小公园总店）</td><td>干面 + 肉丸汤套餐</td><td>¥20【估算】</td></tr>
        <tr><td><b>午餐备选</b></td><td>新关街 9—10 号</td><td>小公园老牌粽球</td><td>双烹粽球</td><td>¥10—15</td></tr>
        <tr><td><b>下午茶</b></td><td>龙眼路 62-1 号</td><td>福铭蚝烙</td><td>蚝烙蘸鱼露，两人分一份</td><td>¥10—20【估算】</td></tr>
        <tr><td><b>下午茶</b></td><td>公园路汇涛花园 1 楼</td><td>张钦德·广场老牌豆花甜汤</td><td>招牌豆花（可让少糖），下午三四点常售罄</td><td>¥6—10</td></tr>
        <tr><td><b>晚餐</b></td><td>公信路 29 号之一</td><td>适口餐厅砂锅粥</td><td>螃蟹鲜虾粥、菜脯煎蛋、爆炒花甲</td><td>¥60【估算】</td></tr>
        <tr><td><b>晚餐备选</b></td><td>朝阳庄北区 12 栋</td><td>富苑饮食（24h）</td><td>白粥打冷、隆江猪脚、鱼饭；生腌只大人浅尝</td><td>¥80—120【估算】</td></tr>
        <tr><td><b>宵夜 · 随意</b></td><td>长平路 33 号 / 桂园 28 幢</td><td>长平老姿娘夜粥（24h）／桂园白粥</td><td>夜糜打冷，谁去谁回，约 23:00 到酒店</td><td>¥60【估算】</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card"><div class="eyebrow">第 4 天 · 早茶与最后一顿牛肉</div>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:13%"><col style="width:17%"><col style="width:24%"><col style="width:28%"><col style="width:18%"></colgroup>
      <thead><tr><th>餐段</th><th>位置</th><th>店</th><th>点什么</th><th>人均</th></tr></thead>
      <tbody>
        <tr><td><b>早餐</b></td><td>凤洲西路凤凰洲公园内</td><td>韩上楼（07:30—20:30）</td><td>潮式茶点、精致潮州菜</td><td>¥60—90【估算】</td></tr>
        <tr><td><b>早餐备选</b></td><td>龙眼南路</td><td>小吴肠粉（二刷）</td><td>全拼肠粉</td><td>¥15</td></tr>
        <tr><td><b>午餐</b></td><td>黄岗路坪东 5 座 1 层</td><td>八合里海记（八合里总店，09:30—23:30）</td><td>吊龙伴、五花趾、手锤牛肉丸</td><td>¥90</td></tr>
        <tr><td><b>午餐备选</b></td><td>金砂西路新荷花园 A 栋</td><td>杏花吴记（09:30—21:30）</td><td>雪花、匙仁、胸口油</td><td>¥104</td></tr>
        <tr><td><b>车上</b></td><td>自备</td><td>D1/D4 买的腐乳饼、绿豆饼、粿品</td><td>垫肚子，别在车站买溢价礼盒</td><td>—</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <div class="eyebrow">升级体验</div>
    <h2>值得多花一点的一两顿</h2>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:30%"><col style="width:48%"><col style="width:22%"></colgroup>
      <thead><tr><th>店</th><th>体验点（不是菜名）</th><th>人均</th></tr></thead>
      <tbody>
        <tr><td><b>富苑饮食</b></td><td>十几米长的打冷自选台，站着指菜，像逛菜市场一样点一顿夜宴</td><td>¥100—150【估算】</td></tr>
        <tr><td><b>载阳茶馆 / 枞馫茶馆</b>（牌坊街）</td><td>老宅里坐下来喝一泡凤凰单丛，偶尔赶上潮剧，逛累了最舒服的落脚点</td><td>¥40—80【估算】</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <div class="eyebrow">品类级必吃 · 11 月时令</div>
    <p style="font-size:.9rem;color:#5C594E">牛肉火锅（现切）、卤鹅（狮头鹅）、蚝烙、肠粉（潮州花生酱 / 汕头酱油两种）、粿条汤与各式粿品、砂锅粥、甘草水果、鸭母捻、反沙芋头、腐乳鸡翅、<b>南澳头水紫菜</b>（11 月采收季）、秋冬海鲜（石斑、膏蟹、生蚝）。<b>找店三看</b>：看坐的是不是本地人、看年头、看点评差评能不能接受；<b>找店口诀</b>：主街看热闹，巷子里吃饭，人多的一般没错。</p>
    <p style="font-size:.8rem;color:#8A8677;margin-top:8px">信源声明：店名／地址／营业时段来自 2026-11-14 联网检索的本地美食长文、大众点评必吃榜转述与 OTA 页面；<b>营业状态与人均未逐家致电核实</b>，到店前用高德／大众点评再看一眼当日状态。人均口径＝一份主菜 + 饮品，非单菜价。</p>
  </div>
</section>

<section id="gift">
  <div class="eyebrow">回来带点啥</div>
  <h2>特产三问卡</h2>
  <table class="tb" style="table-layout:fixed"><colgroup><col style="width:22%"><col style="width:30%"><col style="width:26%"><col style="width:22%"></colgroup>
    <thead><tr><th>特产</th><th>是什么</th><th>哪里买</th><th>好不好带</th></tr></thead>
    <tbody>
      <tr><td><b>腐乳饼 / 绿豆饼</b></td><td>潮州饼食老字号的手信基本款，咸香不腻</td><td>胡荣泉（太平路）、权记饼食（牌坊街）、厚记饼家</td><td>✅ 纸盒装、可寄快递，最省事</td></tr>
      <tr><td><b>凤凰单丛（鸭屎香 / 蜜兰香）</b></td><td>潮州凤凰山乌龙，香型多、被叫「茶中香水」</td><td>市区茶庄或牌坊街茶馆，先试喝再买</td><td>✅ 小罐密封装好带；⚠️ 别买天价礼盒</td></tr>
      <tr><td><b>南澳头水紫菜</b></td><td>11 月正是头水采收季，清甜，干紫菜轻</td><td>后宅镇／云澳镇干货店，别在青澳湾景区摊买</td><td>✅ 干货密封袋，最轻的伴手礼</td></tr>
      <tr><td><b>潮州三宝</b>（老香黄 / 老药桔 / 黄皮豉）</td><td>凉果，可直接吃或冲水，本地人当日常零嘴</td><td>升平路大阳光等老蜜饯店、西马路</td><td>✅ 小瓶装；⚠️ 景区出口溢价明显</td></tr>
      <tr><td><b>牛肉丸 / 真空卤鹅</b></td><td>把潮汕味道带回家的硬通货</td><td>杏花吴记、春梅里、西新市场牛肉丸摊</td><td>⚠️ 需真空 + 保冷，高铁 2.5 小时内可行，到家立刻冷藏</td></tr>
    </tbody>
  </table>
  <p style="font-size:.86rem;color:#5C594E;margin-top:10px">比价提示：景区出口礼盒普遍比市区老店 / 超市贵三成左右；真空肉制品别买散装、别托运；单丛茶认产地直供，不为包装买单。<b>只挑两三样就够</b>，别把最后半天耗在买东西上。</p>
</section>
'''

EB_OK = {
    "总览", "路程", "备选 · 想多玩这样加", "门票 · 预约", "真实场景 · 提前知道", "住宿", "预算", "应急",
    "照着吃就行", "回来带点啥", "特产 · 带一份回家", "提示", "总览 · 行程速览", "路程 · 交通串联",
    "每段开多久", "进门花多少", "心里有数", "可选 · 更从容", "温馨提示",
}
LABEL_STYLE = 'font-size:.62rem;letter-spacing:.24em;color:var(--accent);font-weight:600;margin-bottom:12px'


def fix_eyebrows(s):
    """区块级 eyebrow 用正本措辞；卡片内小标题降级为普通标签，避免自创 eyebrow。"""
    def rep(m):
        txt = m.group(1)
        if txt.strip() in EB_OK:
            return m.group(0)
        return '<div style="' + LABEL_STYLE + '">' + txt + '</div>'
    return re.sub(r'<div class="eyebrow">([^<]*)</div>', rep, s)


CONTENT = fix_eyebrows(CONTENT)

CAM_FIX = {
    "📷 牌坊街：0.5x 广角蹲低，从街心往牌坊序列拍，人少时把孩子放在画面下三分之一。":
        "📷 位置：牌坊街街心｜时段：14:00—15:00｜拍法：0.5x 广角蹲低往牌坊序列拍，把孩子放在画面下三分之一。",
    "📷 长山尾灯塔：0.5x 广角把大桥一起收进去；海风大，手机贴身别举太高。":
        "📷 位置：长山尾灯塔观景台｜时段：12:30—13:30｜拍法：0.5x 广角蹲低把南澳大桥一起收进画面，海风大手机贴身别举太高。",
    "📷 中山纪念亭：站亭子对角，0.5x 仰拍把骑楼弧线收进来；雨天地面的反光别躲，是这天的加分项。":
        "📷 位置：小公园中山纪念亭对角｜时段：10:00—11:00｜拍法：0.5x 仰拍收骑楼弧线，雨天蹲低利用地面反光。",
    "📷 轮渡上隔着玻璃拍对岸，镜头贴玻璃消反光；开「实况」后期转长曝光，水面更平。":
        "📷 位置：广场轮渡右舷｜时段：16:40—17:25｜拍法：镜头贴玻璃消反光，开「实况」后期转长曝光，水面更平。",
}
for _a, _b in CAM_FIX.items():
    CONTENT = CONTENT.replace(_a, _b)

TIPS_EXTRA = '''<div class="card">
    <div style="LABEL_STYLE">拍摄参数速查卡</div>
    <h2>掏出手机就能照做</h2>
    <table class="tb" style="table-layout:fixed"><colgroup><col style="width:28%"><col style="width:36%"><col style="width:36%"></colgroup>
      <thead><tr><th>场景</th><th>iPhone</th><th>安卓</th></tr></thead>
      <tbody>
        <tr><td><b>夜景 · 广济桥灯光秀</b></td><td>夜景模式 3 秒、手肘夹紧靠栏杆，关闪光灯</td><td>专业模式 ISO 400—800、快门 1/4—1s，靠栏杆稳住</td></tr>
        <tr><td><b>日落 · 广场轮渡</b></td><td>开「实况」，后期转长曝光</td><td>点测光对太阳外侧，曝光补偿 −0.3</td></tr>
        <tr><td><b>雨景 · 小公园骑楼</b></td><td>躲进连廊、镜头贴玻璃消反光</td><td>蹲低 0.5x 收地面倒影，别开闪光灯</td></tr>
        <tr><td><b>美食 · 火锅俯拍</b></td><td>1x 垂直向下、关闪光灯用店内暖光</td><td>0.5x 会变形，改 1x 并手动降一档曝光</td></tr>
        <tr><td><b>孩子抓拍 · 沙滩 / 骑楼</b></td><td>连拍 + 人像模式 1x</td><td>开运动追焦，别喊「看镜头」</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <div style="LABEL_STYLE">雨天方案</div>
    <p style="font-size:.9rem;color:#5C594E">11/18 确认中雨以上或 6 级以上阵风＝南澳整段取消，改市区室内线；11/19 降温阵雨＝骑楼、开埠陈列馆、茶馆、砂锅粥为主，午休照留；11/20 只剩 12℃ 时全部安排在室内与车上。逐日的具体处置写在各天卡片尾部的「🛟 当天 Plan B」，此处不重复。</p>
  </div>
'''.replace('LABEL_STYLE', LABEL_STYLE)
CONTENT = re.sub(
    r'(<section id="tips">[\s\S]*?)</section>',
    lambda m: m.group(1) + '\n' + TIPS_EXTRA + '\n</section>',
    CONTENT, count=1)

HEAD = '''<!doctype html>
<html lang="zh-CN" data-skeleton-version="1.19.1">
<!-- skeleton-version: 1.19.1 -->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="generator" content="jianhao-travel-planner · 基准骨架 · 指纹 134ca5b45d">
<title>潮汕 4 天路书 · 一家三口（朋友版）</title>
<script>document.documentElement.classList.add('js');</script>
''' + CSS + '''
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
    <div class="logo">潮汕<span>.</span></div>
    <div class="logo-sub">4 天 3 晚 · 一家三口 · 自驾版</div>
  </div>
  <nav aria-label="页面导航">
    <div class="nav-group">
      <div class="nav-label">行程</div>
      <a href="#overview">总览</a>
      <a href="#drive">路程</a>
      <a href="#day1">第 1 天 · 潮州古城</a>
      <a href="#day2">第 2 天 · 南澳岛</a>
      <a href="#day3">第 3 天 · 汕头老城</a>
      <a href="#day4">第 4 天 · 回家</a>
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
    深圳出发 · 2026-11-17 — 11-20<br>
    2 成人 + 1 名小学生<br>
    信息 2026-11-14 实查
  </div>
</aside>
<main id="main"><div class="wrap">
'''

FOOT = '''<footer style="padding:64px 0 80px;text-align:center">
  <h2>潮汕 4 天路书 · 一家三口（朋友版）</h2>
  <p>深圳出发 · 2026-11-17 — 11-20 · 高铁往返 + 落地自驾<br>本地单文件 · 无外部依赖 · 断网可打开<br>信息 2026-11-14 联网实查 · 未核实项已标注</p>
  <p>配图：8 张全部为手绘示意插画（非当地实景照片），逐张标注「（示意）」；图源＝本文件内嵌 SVG，无外部图片。<br>动线图 5 张为自绘示意，非等比例，实际以导航为准。</p>
  <p style="margin-top:18px;font-weight:700">方案仅供参考——<br>安全和开心，才是最重要的。🌕</p>
  <p style="font-size:.8rem;color:#8A8677;margin-top:10px">路上累了就在服务区歇歇，别着急；行程随时按当天状态调整，少看一个景点不亏，家人舒服才值。</p>
</footer>
<div class="tailpad" style="height:96px" aria-hidden="true"></div>
</div></main>
<button class="backtop" id="backtop" aria-label="回到顶部">↑</button>
''' + JS_ALL + '''
</body>
</html>
'''

html = HEAD + CONTENT + FOOT
out = HERE.parent / "cs.html"
out.write_text(html, encoding="utf-8")
print("written:", out, len(html), "chars")
print("figures:", html.count("<figure>"), "sections:", len(re.findall(r'<section id="', html)))
