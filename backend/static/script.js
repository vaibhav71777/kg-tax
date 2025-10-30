const form = document.getElementById("taxForm");
const resultCard = document.getElementById("result");
const taxAmount = document.getElementById("taxAmount");
const recList = document.getElementById("recs");

// Set your backend URL here (Railway backend endpoint)
const API_URL = "https://your-backend-url.up.railway.app/calculate";

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const income = parseFloat(document.getElementById("income").value);
  const age = parseInt(document.getElementById("age").value);
  const regime = document.getElementById("regime").value;

  const payload = { income, age, regime };

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await res.json();
    taxAmount.textContent = `₹ ${data.tax.toLocaleString("en-IN")}`;
    recList.innerHTML = "";
    data.recommendations.forEach((r) => {
      const li = document.createElement("li");
      li.textContent = r;
      recList.appendChild(li);
    });
    resultCard.classList.remove("hidden");
  } catch (err) {
    alert("Error connecting to backend.");
    console.error(err);
  }
});
