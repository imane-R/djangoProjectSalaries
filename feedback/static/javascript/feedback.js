// static/feedback/feedback.js

document.addEventListener("DOMContentLoaded", function () {
  const jobId = document.getElementById("feedback-form").dataset.jobid;

  // Charger les feedbacks
  fetch(`/api/feedbacks/?job=${jobId}`)
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("feedback-list");
      data.forEach(feedback => {
        const item = document.createElement("div");
        item.className = "bg-white p-4 rounded shadow mb-2";
        item.innerHTML = `<strong>${feedback.author_name}</strong> (${feedback.rating}/5) <br>${feedback.comment}`;
        container.appendChild(item);
      });
    });

  // Gérer le POST
  const form = document.getElementById("feedback-form");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(form);
    const data = {
      job: parseInt(jobId),
      author_name: formData.get("author_name"),
      rating: parseInt(formData.get("rating")),
      comment: formData.get("comment")
    };

    fetch("/api/feedbacks/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => {
        if (res.ok) return res.json();
        throw new Error("Erreur lors de l’envoi");
      })
      .then(newFeedback => {
        form.reset();
        location.reload();  // Ou appelle à nouveau la fonction de fetch
      })
      .catch(err => alert(err));
  });
});
