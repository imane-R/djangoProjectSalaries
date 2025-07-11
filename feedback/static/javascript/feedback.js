document.addEventListener("DOMContentLoaded", () => {
  const select = document.getElementById("job-select");
  const title = document.getElementById("job-title");
  const list = document.getElementById("feedback-list");
  const ratingText = document.getElementById("avg-rating");

  async function loadFeedbacks(jobId, jobName) {
    try {
      const response = await fetch(`/api/feedbacks/?job=${jobId}`);
      const data = await response.json();

      title.textContent = `Feedbacks pour : ${jobName}`;

      // Moyenne des notes
      let sum = 0;
      data.forEach(fb => sum += fb.rating);
      ratingText.textContent = data.length
        ? `Note moyenne : ${(sum / data.length).toFixed(1)} / 5`
        : "Aucun feedback.";

      list.innerHTML = data.map(fb => `
        <div class="p-4 bg-white rounded shadow">
          <p><strong>Auteur :</strong> ${fb.author_name}</p>
          <p><strong>Commentaire :</strong> ${fb.comment}</p>
          <p><strong>Note :</strong> ${fb.rating}</p>
        </div>
      `).join('');
    } catch (error) {
      console.error("Erreur lors du chargement des feedbacks :", error);
    }
  }

  // Charge le premier job au démarrage
  if (select.options.length > 0) {
    const id = select.value;
    const label = select.options[select.selectedIndex].text;
    loadFeedbacks(id, label);
  }

  // Changement de poste
  select.addEventListener("change", () => {
    const id = select.value;
    const label = select.options[select.selectedIndex].text;
    loadFeedbacks(id, label);
  });
});

// post
const form = document.getElementById("feedback-form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const jobId = form.dataset.jobid;

  const payload = {
    author_name: form.author_name.value,
    rating: form.rating.value,
    comment: form.comment.value,
    job: jobId
  };

  const response = await fetch("/api/feedbacks/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Token 754007e78ddac7d2bc1cbbe4496671ff4069a186"  // ← ici nécessaire !
    },
    body: JSON.stringify(payload)
  });

  if (response.ok) {
    form.reset();
    alert("Feedback ajouté !");
    // Recharge les feedbacks après envoi
    const label = document.querySelector(`#job-select option[value="${jobId}"]`).textContent;
    loadFeedbacks(jobId, label);
  } else {
    alert("Erreur lors de l'envoi du feedback.");
  }
});
