/* LOGIN */
const loginBtn = document.getElementById("loginBtn");
const loginBox = document.getElementById("loginBox");
const dashboard = document.getElementById("dashboard");

loginBtn.onclick = () => {
  loginBox.style.display = "none";
  dashboard.style.display = "block";

  const role = document.getElementById("role").value;
  document.getElementById("doctorPanel").style.display =
    role === "doctor" ? "block" : "none";
  document.getElementById("patientPanel").style.display =
    role === "patient" ? "block" : "none";
};

/* ❤️ ECG */
const ecg = document.getElementById("ecg");
const ctx = ecg.getContext("2d");
let bpm = 72;
let x = 0;

setInterval(() => {
  ctx.clearRect(0,0,400,120);
  ctx.strokeStyle = "#00ff66";
  ctx.beginPath();

  for(let i=0;i<400;i++){
    let y = 60 + Math.sin((i+x)/10)*20;
    ctx.lineTo(i,y);
  }

  ctx.stroke();
  x += 2;

  bpm += Math.random() > 0.5 ? 1 : -1;
  bpm = Math.max(60, Math.min(120, bpm));
  document.getElementById("bpm").textContent = bpm;
}, 500);

/* 🫁 Oxygen */
const ring = document.querySelector(".progress");
const spo2Text = document.getElementById("spo2Text");
let spo2 = 98;

setInterval(() => {
  spo2 += Math.random() > 0.5 ? 1 : -1;
  spo2 = Math.max(92, Math.min(99, spo2));
  spo2Text.textContent = spo2 + "%";

  ring.style.strokeDashoffset = 314 - (314 * spo2 / 100);
}, 2000);
