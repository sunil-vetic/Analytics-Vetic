<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vetic Pet Care — Live Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
<style>
:root {
  --bg:#0a0a0f; --bg2:#111118; --bg3:#18181f;
  --border:rgba(255,255,255,0.07); --border2:rgba(255,255,255,0.13);
  --text:#f0efe8; --text2:#8a8a9a; --text3:#4a4a5a;
  --purple:#7f6fff; --teal:#1fcf8e; --coral:#ff6b4a; --blue:#4a9eff; --amber:#f5a623;
  --font:'Syne',sans-serif; --mono:'DM Mono',monospace;
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:var(--font);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(127,111,255,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(127,111,255,0.03) 1px,transparent 1px);background-size:40px 40px;pointer-events:none;z-index:0;}

.wrap{max-width:1240px;margin:0 auto;padding:28px 20px;position:relative;z-index:1;}

/* HEADER */
.header{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;flex-wrap:wrap;gap:14px;}
.brand{display:flex;align-items:center;gap:12px;}
.brand-icon{width:42px;height:42px;background:var(--purple);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:22px;}
.brand-name{font-size:20px;font-weight:700;letter-spacing:-0.5px;}
.brand-sub{font-size:11px;color:var(--text2);font-family:var(--mono);margin-top:2px;}

.header-actions{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}

.status-pill{display:flex;align-items:center;gap:6px;background:var(--bg3);border:1px solid var(--border2);border-radius:100px;padding:6px 14px;font-size:11px;font-family:var(--mono);color:var(--text2);}
.sdot{width:7px;height:7px;border-radius:50%;background:var(--text3);transition:background 0.4s;}
.sdot.live{background:var(--teal);box-shadow:0 0 6px var(--teal);}
.sdot.error{background:var(--coral);}
.sdot.loading{background:var(--amber);animation:blink 1s infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}

/* BIG REFRESH BUTTON */
.btn-refresh-big{
  display:flex;align-items:center;gap:8px;
  background:var(--purple);color:#fff;
  border:none;border-radius:10px;
  font-family:var(--mono);font-size:13px;font-weight:500;
  padding:10px 20px;cursor:pointer;
  transition:all 0.2s;
  white-space:nowrap;
}
.btn-refresh-big:hover{background:#6a5ce8;transform:translateY(-1px);}
.btn-refresh-big:active{transform:scale(0.97);}
.btn-refresh-big svg{width:15px;height:15px;flex-shrink:0;}
.btn-refresh-big.spinning svg{animation:spin 0.8s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}

.sync-info{font-size:11px;font-family:var(--mono);color:var(--text3);}
.countdown{color:var(--purple);font-weight:500;}

/* ERROR */
.err{display:none;background:rgba(255,107,74,0.08);border:1px solid rgba(255,107,74,0.25);border-radius:10px;padding:14px 18px;font-size:12px;color:#ff9980;margin-bottom:20px;font-family:var(--mono);line-height:1.7;}

/* METRICS */
.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(155px,1fr));gap:11px;margin-bottom:24px;}
.mcard{background:var(--bg2);border:1px solid var(--border);border-radius:12px;padding:16px 18px;position:relative;overflow:hidden;transition:border-color 0.2s;}
.mcard:hover{border-color:var(--border2);}
.mcard::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--ac,var(--purple));opacity:0.7;}
.mlabel{font-size:10px;font-family:var(--mono);color:var(--text3);text-transform:uppercase;letter-spacing:0.07em;margin-bottom:8px;}
.mval{font-size:24px;font-weight:700;letter-spacing:-1px;line-height:1;}
.msub{font-size:10px;color:var(--text3);font-family:var(--mono);margin-top:5px;}

/* CHARTS */
.charts-2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;}
.cpanel{background:var(--bg2);border:1px solid var(--border);border-radius:12px;padding:18px 20px;}
.cpanel.full{grid-column:1/-1;}
.ptitle{font-size:13px;font-weight:500;margin-bottom:3px;}
.psub{font-size:10px;font-family:var(--mono);color:var(--text3);margin-bottom:14px;}
.legend{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:10px;}
.li{display:flex;align-items:center;gap:5px;font-size:10px;font-family:var(--mono);color:var(--text2);}
.ld{width:8px;height:8px;border-radius:2px;flex-shrink:0;}
.cw{position:relative;}

/* SKELETON */
.skel{background:linear-gradient(90deg,var(--bg3) 25%,var(--bg2) 50%,var(--bg3) 75%);background-size:200% 100%;animation:shimmer 1.5s infinite;border-radius:8px;}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}

/* ===== AI COPILOT PANEL ===== */
.copilot-section{margin-top:24px;}
.copilot-header{display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.copilot-badge{display:flex;align-items:center;gap:7px;background:linear-gradient(135deg,rgba(127,111,255,0.15),rgba(31,207,142,0.1));border:1px solid rgba(127,111,255,0.3);border-radius:100px;padding:6px 14px;font-size:11px;font-family:var(--mono);color:var(--purple);}
.copilot-badge-dot{width:7px;height:7px;border-radius:50%;background:var(--teal);animation:blink 2s infinite;}
.copilot-title{font-size:15px;font-weight:500;}
.copilot-sub{font-size:11px;color:var(--text3);font-family:var(--mono);}

.copilot-body{background:var(--bg2);border:1px solid rgba(127,111,255,0.2);border-radius:14px;overflow:hidden;}

/* Suggested questions */
.suggestions{display:flex;flex-wrap:wrap;gap:8px;padding:16px 18px 0;}
.sq{background:var(--bg3);border:1px solid var(--border2);border-radius:8px;padding:7px 13px;font-size:11px;font-family:var(--mono);color:var(--text2);cursor:pointer;transition:all 0.2s;}
.sq:hover{border-color:var(--purple);color:var(--purple);background:rgba(127,111,255,0.08);}

/* Chat messages */
.chat-msgs{padding:16px 18px;min-height:120px;max-height:420px;overflow-y:auto;display:flex;flex-direction:column;gap:14px;}
.msg{display:flex;gap:10px;align-items:flex-start;}
.msg.user{flex-direction:row-reverse;}
.msg-avatar{width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0;}
.msg.ai .msg-avatar{background:rgba(127,111,255,0.2);color:var(--purple);}
.msg.user .msg-avatar{background:rgba(31,207,142,0.15);color:var(--teal);}
.msg-bubble{max-width:85%;padding:10px 14px;border-radius:10px;font-size:13px;line-height:1.6;}
.msg.ai .msg-bubble{background:var(--bg3);border:1px solid var(--border);color:var(--text);}
.msg.user .msg-bubble{background:rgba(127,111,255,0.12);border:1px solid rgba(127,111,255,0.2);color:var(--text);}
.msg-bubble p{margin:0 0 6px;}
.msg-bubble p:last-child{margin:0;}
.msg-bubble strong{color:var(--purple);font-weight:500;}

.typing-indicator{display:none;align-items:center;gap:4px;padding:10px 14px;}
.typing-dot{width:6px;height:6px;border-radius:50%;background:var(--text3);animation:tdot 1.2s infinite;}
.typing-dot:nth-child(2){animation-delay:0.2s;}
.typing-dot:nth-child(3){animation-delay:0.4s;}
@keyframes tdot{0%,80%,100%{transform:scale(0.8);opacity:0.5}40%{transform:scale(1.1);opacity:1}}

/* Chat input */
.chat-input-area{display:flex;align-items:center;gap:10px;padding:14px 18px;border-top:1px solid var(--border);}
.chat-input{flex:1;background:var(--bg3);border:1px solid var(--border2);border-radius:9px;padding:9px 14px;color:var(--text);font-family:var(--mono);font-size:12px;outline:none;transition:border-color 0.2s;}
.chat-input:focus{border-color:var(--purple);}
.chat-input::placeholder{color:var(--text3);}
.btn-send{background:var(--purple);border:none;border-radius:8px;width:34px;height:34px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all 0.2s;flex-shrink:0;}
.btn-send:hover{background:#6a5ce8;}
.btn-send:disabled{background:var(--bg3);cursor:not-allowed;}
.btn-send svg{width:15px;height:15px;color:#fff;}

/* FOOTER */
.footer{margin-top:28px;padding-top:18px;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;}
.footer-text{font-size:10px;font-family:var(--mono);color:var(--text3);}
.footer-link{font-size:10px;font-family:var(--mono);color:var(--purple);text-decoration:none;opacity:0.7;}
.footer-link:hover{opacity:1;}

@media(max-width:640px){
  .charts-2{grid-template-columns:1fr;}
  .cpanel.full{grid-column:1;}
  .header{flex-direction:column;align-items:flex-start;}
}
</style>
</head>
<body>
<div class="wrap">

  <!-- HEADER -->
  <div class="header">
    <div class="brand">
      <div class="brand-icon">🐾</div>
      <div>
        <div class="brand-name">Vetic Pet Care</div>
        <div class="brand-sub">Live Analytics · new_app_event_data</div>
      </div>
    </div>
    <div class="header-actions">
      <div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px;">
        <div class="status-pill">
          <div class="sdot loading" id="sdot"></div>
          <span id="stext">Connecting...</span>
        </div>
        <div class="sync-info" id="lastSync"></div>
        <div class="sync-info">Auto-refresh in <span class="countdown" id="countdown">60:00</span></div>
      </div>
      <button class="btn-refresh-big" id="refreshBtn" onclick="manualRefresh()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M23 4v6h-6"/><path d="M1 20v-6h6"/>
          <path d="M3.51 9a9 9 0 0114.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0020.49 15"/>
        </svg>
        Refresh Data
      </button>
    </div>
  </div>

  <div class="err" id="errBanner"></div>

  <!-- METRICS -->
  <div class="metrics" id="metricsGrid">
    <div class="mcard skel" style="height:86px;"></div>
    <div class="mcard skel" style="height:86px;"></div>
    <div class="mcard skel" style="height:86px;"></div>
    <div class="mcard skel" style="height:86px;"></div>
    <div class="mcard skel" style="height:86px;"></div>
    <div class="mcard skel" style="height:86px;"></div>
  </div>

  <!-- CHARTS ROW 1 -->
  <div class="charts-2">
    <div class="cpanel">
      <div class="ptitle">Conversion funnel</div>
      <div class="psub">users → session → intent → cart</div>
      <div class="cw" style="height:230px;"><canvas id="funnelChart" role="img" aria-label="Conversion funnel"></canvas></div>
    </div>
    <div class="cpanel">
      <div class="ptitle">Intent breakdown</div>
      <div class="psub">what users browsed</div>
      <div class="legend" id="intentLegend"></div>
      <div class="cw" style="height:195px;"><canvas id="intentChart" role="img" aria-label="Intent donut"></canvas></div>
    </div>
  </div>

  <!-- CHARTS ROW 2 -->
  <div class="charts-2">
    <div class="cpanel">
      <div class="ptitle">Intent → cart conversion</div>
      <div class="psub">by product category</div>
      <div class="legend">
        <div class="li"><div class="ld" style="background:#1fcf8e;"></div>Intent</div>
        <div class="li"><div class="ld" style="background:#4a5568;"></div>Add to cart</div>
      </div>
      <div class="cw" style="height:170px;"><canvas id="convChart" role="img" aria-label="Intent vs cart"></canvas></div>
    </div>
    <div class="cpanel">
      <div class="ptitle">Engagement rates</div>
      <div class="psub">% of total users</div>
      <div class="cw" style="height:210px;"><canvas id="rateChart" role="img" aria-label="Engagement rates"></canvas></div>
    </div>
  </div>

  <!-- CLINICS CHART -->
  <div class="charts-2" style="margin-bottom:0;">
    <div class="cpanel full">
      <div class="ptitle">Top 10 clinics by user volume</div>
      <div class="psub">clinic-associated sessions only</div>
      <div class="cw" style="height:420px;"><canvas id="clinicChart" role="img" aria-label="Top clinics"></canvas></div>
    </div>
  </div>

  <!-- AI COPILOT -->
  <div class="copilot-section">
    <div class="copilot-header">
      <div class="copilot-badge">
        <div class="copilot-badge-dot"></div>
        AI Copilot
      </div>
      <div>
        <div class="copilot-title">Ask anything about your data</div>
        <div class="copilot-sub">Powered by Claude · Understands your live metrics</div>
      </div>
    </div>

    <div class="copilot-body">
      <div class="suggestions" id="suggestions">
        <div class="sq" onclick="askSuggestion(this)">What's my overall conversion rate?</div>
        <div class="sq" onclick="askSuggestion(this)">Which category has the worst cart drop-off?</div>
        <div class="sq" onclick="askSuggestion(this)">Which city is performing best?</div>
        <div class="sq" onclick="askSuggestion(this)">How can I improve add-to-cart rate?</div>
        <div class="sq" onclick="askSuggestion(this)">What % of users are not logging in?</div>
        <div class="sq" onclick="askSuggestion(this)">Give me a QA summary of today's data</div>
      </div>

      <div class="chat-msgs" id="chatMsgs">
        <div class="msg ai">
          <div class="msg-avatar">✦</div>
          <div class="msg-bubble">Hi! I'm your data copilot. I can see your live Vetic Pet Care metrics — ask me anything about sessions, intents, cart performance, clinic rankings, or data quality. Try a suggestion above or type your own question.</div>
        </div>
      </div>

      <div class="typing-indicator" id="typingIndicator">
        <div class="msg-avatar" style="width:28px;height:28px;border-radius:8px;background:rgba(127,111,255,0.2);display:flex;align-items:center;justify-content:center;font-size:13px;">✦</div>
        <div style="display:flex;align-items:center;gap:4px;padding:10px 14px;background:var(--bg3);border:1px solid var(--border);border-radius:10px;">
          <div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>
        </div>
      </div>

      <div class="chat-input-area">
        <input class="chat-input" id="chatInput" type="text" placeholder="Ask about your data... e.g. why is accessories cart rate low?" onkeydown="if(event.key==='Enter')sendChat()">
        <button class="btn-send" id="sendBtn" onclick="sendChat()">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="footer-text">Source: Google Sheets · Tab: new_app_event_data · Auto-refresh every 60 min</div>
    <a class="footer-link" href="https://docs.google.com/spreadsheets/d/1GbYNBZ3fl7ctmYuy1T4h-WgCoXb098804s0zy2fQG8E/edit?gid=1575033653" target="_blank">Open source sheet ↗</a>
  </div>

</div>

<script>
const SHEET_ID = '1GbYNBZ3fl7ctmYuy1T4h-WgCoXb098804s0zy2fQG8E';
const GID = '1575033653';
const CSV_URL = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?format=csv&gid=${GID}`;
const REFRESH_MS = 60 * 60 * 1000;

let charts = {}, cdInterval, nextRefresh, currentData = null, chatHistory = [];

/* -------- STATUS -------- */
function setStatus(state, text) {
  document.getElementById('sdot').className = 'sdot ' + state;
  document.getElementById('stext').textContent = text;
}

function showErr(msg) {
  const el = document.getElementById('errBanner');
  el.style.display = 'block';
  el.innerHTML = `<strong>Could not fetch data.</strong> ${msg}<br>Check that your Google Sheet sharing is set to <em>"Anyone with the link → Viewer"</em>, then hit Refresh Data.`;
}
function hideErr() { document.getElementById('errBanner').style.display = 'none'; }

/* -------- UTILS -------- */
function fmt(n) {
  if (n >= 1e6) return (n/1e6).toFixed(1)+'M';
  if (n >= 1000) return (n/1000).toFixed(1)+'k';
  return String(Math.round(n));
}
function pct(a,b) { return b ? (a/b*100).toFixed(1)+'%' : '0%'; }

/* -------- METRICS -------- */
function buildMetrics(d) {
  const cards = [
    {label:'Total users',     val:d.total.toLocaleString(), sub:'tracked today',             ac:'#7f6fff'},
    {label:'Session rate',    val:pct(d.sessions,d.total),  sub:fmt(d.sessions)+' sessions', ac:'#1fcf8e'},
    {label:'Login rate',      val:pct(d.loggedIn,d.total),  sub:fmt(d.loggedIn)+' logged in',ac:'#4a9eff'},
    {label:'Clinic-linked',   val:fmt(d.clinicUsers),        sub:pct(d.clinicUsers,d.total), ac:'#f5a623'},
    {label:'Add to cart',     val:fmt(d.atc),                sub:'cart rate '+pct(d.atc,d.total), ac:'#ff6b4a'},
    {label:'With intent',     val:fmt(d.si),                 sub:'intent rate '+pct(d.si,d.total), ac:'#7f6fff'},
  ];
  document.getElementById('metricsGrid').innerHTML = cards.map(c =>
    `<div class="mcard" style="--ac:${c.ac}"><div class="mlabel">${c.label}</div><div class="mval">${c.val}</div><div class="msub">${c.sub}</div></div>`
  ).join('');
}

/* -------- CHARTS -------- */
const TC = 'rgba(255,255,255,0.38)', GC = 'rgba(255,255,255,0.05)';
const baseO = { responsive:true, maintainAspectRatio:false, plugins:{legend:{display:false}}, animation:{duration:500,easing:'easeOutQuart'} };

function dk(id){ if(charts[id]){charts[id].destroy();delete charts[id];} }
function mk(id,cfg){ dk(id); charts[id]=new Chart(document.getElementById(id),cfg); }
const ax = (extra={})=>({ ticks:{color:TC,font:{size:10},...(extra.ticks||{})}, grid:{color:GC}, border:{color:'transparent'}, ...extra });

function buildCharts(d) {
  const {total,sessions,si,atc,foodI,medI,accI,foodC,medC,accC,topClinics,loggedIn,clinicUsers} = d;

  mk('funnelChart',{type:'bar',data:{labels:['Total','Sessions','Intent','Cart'],datasets:[{data:[total,sessions,si,atc],backgroundColor:['#7f6fff','#1fcf8e','#4a9eff','#ff6b4a'],borderRadius:6,borderSkipped:false}]},
    options:{...baseO,scales:{x:ax({ticks:{color:TC,font:{size:11},autoSkip:false,maxRotation:0}}),y:ax({ticks:{color:TC,font:{size:10},callback:v=>fmt(v)}})}}});

  const iT=foodI+medI+accI;
  document.getElementById('intentLegend').innerHTML=[['#1fcf8e','Food',pct(foodI,iT)],['#4a9eff','Medicine',pct(medI,iT)],['#ff6b4a','Accessories',pct(accI,iT)]]
    .map(([c,l,p])=>`<div class="li"><div class="ld" style="background:${c};"></div>${l} ${p}</div>`).join('');
  mk('intentChart',{type:'doughnut',data:{labels:['Food','Medicine','Accessories'],datasets:[{data:[foodI,medI,accI],backgroundColor:['#1fcf8e','#4a9eff','#ff6b4a'],borderWidth:0,hoverOffset:8}]},
    options:{...baseO,cutout:'65%',plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>' '+c.label+': '+c.parsed.toLocaleString()}}}}});

  mk('convChart',{type:'bar',data:{labels:['Food','Medicine','Accessories'],datasets:[
    {label:'Intent',data:[foodI,medI,accI],backgroundColor:'#1fcf8e',borderRadius:4},
    {label:'Cart',data:[foodC,medC,accC],backgroundColor:'#4a5568',borderRadius:4}]},
    options:{...baseO,scales:{x:ax(),y:ax({ticks:{color:TC,font:{size:10},callback:v=>fmt(v)}})}}});

  mk('rateChart',{type:'bar',data:{labels:['Session','Login','Clinic','Intent','Cart'],datasets:[{
    data:[+(sessions/total*100).toFixed(1),+(loggedIn/total*100).toFixed(1),+(clinicUsers/total*100).toFixed(1),+(si/total*100).toFixed(1),+(atc/total*100).toFixed(1)],
    backgroundColor:['#7f6fff','#1fcf8e','#4a9eff','#f5a623','#ff6b4a'],borderRadius:6,borderSkipped:false}]},
    options:{...baseO,scales:{x:ax({ticks:{color:TC,font:{size:10},autoSkip:false,maxRotation:0}}),y:ax({ticks:{color:TC,font:{size:10},callback:v=>v+'%'},max:100})}}});

  mk('clinicChart',{type:'bar',data:{labels:topClinics.map(([k])=>k.length>48?k.slice(0,48)+'…':k),datasets:[{label:'Users',data:topClinics.map(([,v])=>v),backgroundColor:'#7f6fff',borderRadius:4}]},
    options:{...baseO,indexAxis:'y',scales:{x:ax({ticks:{color:TC,font:{size:11},callback:v=>fmt(v)}}),y:ax({ticks:{color:TC,font:{size:10},autoSkip:false},grid:{color:'transparent'}})}}});
}

/* -------- DATA LOADING -------- */
function processRows(rows) {
  const total=rows.length,
    loggedIn=rows.filter(r=>r.user_id&&r.user_id!=='N/A'&&r.user_id.trim()!=='').length,
    clinicUsers=rows.filter(r=>r.clinic_billed_clinic&&r.clinic_billed_clinic.trim()).length,
    sessions=rows.filter(r=>r.session_start==='1').length,
    foodI=rows.filter(r=>r.food_intent==='1').length,
    medI=rows.filter(r=>r.medicine_intent==='1').length,
    accI=rows.filter(r=>r.accessories_intent==='1').length,
    foodC=rows.filter(r=>r.food_add_to_cart==='1').length,
    medC=rows.filter(r=>r.medicine_add_to_cart==='1').length,
    accC=rows.filter(r=>r.accessories_add_to_cart==='1').length,
    si=rows.filter(r=>r.SI==='1').length,
    atc=rows.filter(r=>r.add_to_cart==='1').length;
  const cc={};
  rows.forEach(r=>{if(r.clinic_billed_clinic&&r.clinic_billed_clinic.trim())cc[r.clinic_billed_clinic.trim()]=(cc[r.clinic_billed_clinic.trim()]||0)+1;});
  const topClinics=Object.entries(cc).sort((a,b)=>b[1]-a[1]).slice(0,10);
  return {total,loggedIn,clinicUsers,sessions,foodI,medI,accI,foodC,medC,accC,si,atc,topClinics};
}

function startCountdown() {
  if(cdInterval)clearInterval(cdInterval);
  nextRefresh=Date.now()+REFRESH_MS;
  cdInterval=setInterval(()=>{
    const rem=Math.max(0,nextRefresh-Date.now());
    const m=Math.floor(rem/60000),s=Math.floor((rem%60000)/1000);
    document.getElementById('countdown').textContent=String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');
    if(rem===0)loadData();
  },1000);
}

async function loadData() {
  setStatus('loading','Fetching live data...');
  hideErr();
  const btn=document.getElementById('refreshBtn');
  btn.classList.add('spinning');
  try {
    const res=await fetch(CSV_URL+'&cb='+Date.now());
    if(!res.ok)throw new Error('HTTP '+res.status+' — check sheet permissions');
    const text=await res.text();
    const parsed=Papa.parse(text,{header:true,skipEmptyLines:true});
    if(!parsed.data.length)throw new Error('Sheet returned 0 rows');
    currentData=processRows(parsed.data);
    buildMetrics(currentData);
    buildCharts(currentData);
    const now=new Date();
    document.getElementById('lastSync').textContent='Synced '+now.toLocaleTimeString()+' · '+currentData.total.toLocaleString()+' rows';
    setStatus('live','Live · '+parsed.data.length.toLocaleString()+' rows');
    startCountdown();
  } catch(e) {
    setStatus('error','Fetch failed');
    showErr(e.message);
  } finally {
    btn.classList.remove('spinning');
  }
}

function manualRefresh() {
  if(cdInterval)clearInterval(cdInterval);
  loadData();
}

setInterval(loadData, REFRESH_MS);
loadData();

/* ========== AI COPILOT ========== */
function buildContext() {
  if(!currentData) return 'No data loaded yet.';
  const d=currentData;
  return `You are a data analyst copilot for Vetic Pet Care. Here is today's live data summary:

METRICS:
- Total users: ${d.total.toLocaleString()}
- Sessions started: ${d.sessions.toLocaleString()} (${pct(d.sessions,d.total)} of users)
- Logged-in users: ${d.loggedIn.toLocaleString()} (${pct(d.loggedIn,d.total)})
- Clinic-linked users: ${d.clinicUsers.toLocaleString()} (${pct(d.clinicUsers,d.total)})
- Users with any intent: ${d.si.toLocaleString()} (${pct(d.si,d.total)})
- Add-to-cart: ${d.atc.toLocaleString()} (${pct(d.atc,d.total)})

INTENT SIGNALS:
- Food intent: ${d.foodI.toLocaleString()} → food add-to-cart: ${d.foodC.toLocaleString()} (${pct(d.foodC,d.foodI)} conversion)
- Medicine intent: ${d.medI.toLocaleString()} → medicine add-to-cart: ${d.medC.toLocaleString()} (${pct(d.medC,d.medI)} conversion)
- Accessories intent: ${d.accI.toLocaleString()} → accessories add-to-cart: ${d.accC.toLocaleString()} (${pct(d.accC,d.accI)} conversion)

TOP CLINICS:
${d.topClinics.map(([name,count],i)=>`${i+1}. ${name}: ${count.toLocaleString()} users`).join('\n')}

Answer questions clearly and concisely. Use bullet points where helpful. Reference specific numbers from the data above. If asked for QA issues, look for anomalies like very low conversion rates, high drop-offs, or missing data patterns.`;
}

function appendMsg(role, html) {
  const msgs=document.getElementById('chatMsgs');
  const div=document.createElement('div');
  div.className='msg '+role;
  div.innerHTML=`<div class="msg-avatar">${role==='ai'?'✦':'U'}</div><div class="msg-bubble">${html}</div>`;
  msgs.appendChild(div);
  msgs.scrollTop=msgs.scrollHeight;
}

function setTyping(show) {
  const el=document.getElementById('typingIndicator');
  el.style.display=show?'flex':'none';
  if(show) document.getElementById('chatMsgs').scrollTop=9999;
}

function escHtml(s){
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function formatAIResponse(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>')
    .replace(/\*(.*?)\*/g,'<em>$1</em>')
    .replace(/^- (.+)$/gm,'<li>$1</li>')
    .replace(/(<li>.*<\/li>)/gs,'<ul style="margin:6px 0 6px 14px;display:flex;flex-direction:column;gap:3px;">$1</ul>')
    .replace(/\n\n/g,'</p><p>')
    .replace(/\n/g,'<br>')
    .replace(/^(.)/,'<p>$1')
    .replace(/(.)$/,'$1</p>');
}

async function sendChat(question) {
  const input=document.getElementById('chatInput');
  const q=(question||input.value).trim();
  if(!q)return;

  input.value='';
  document.getElementById('sendBtn').disabled=true;

  appendMsg('user', escHtml(q));
  chatHistory.push({role:'user',content:q});
  setTyping(true);

  try {
    const systemPrompt=buildContext();
    const messages=chatHistory.slice(-10);

    const res=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:1000,
        system:systemPrompt,
        messages:messages
      })
    });

    const data=await res.json();
    const reply=data.content?.[0]?.text||'Sorry, I could not get a response.';
    chatHistory.push({role:'assistant',content:reply});
    setTyping(false);
    appendMsg('ai',formatAIResponse(reply));
  } catch(e) {
    setTyping(false);
    appendMsg('ai','<span style="color:#ff9980;">Error reaching AI. Check your network connection.</span>');
  }

  document.getElementById('sendBtn').disabled=false;
  document.getElementById('chatInput').focus();
}

function askSuggestion(el) {
  sendChat(el.textContent);
}
</script>
</body>
</html>
