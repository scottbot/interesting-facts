(function () {
  "use strict";

  const card = document.getElementById("fact-card");
  const quote = document.getElementById("fact");
  const authorName = document.getElementById("author-name");
  const authorHandle = document.getElementById("author-handle");

  fetch("data/facts.json")
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Could not load facts.");
      }
      return response.json();
    })
    .then(function (facts) {
      if (!Array.isArray(facts) || facts.length === 0) {
        throw new Error("No facts were found.");
      }

      const selected = facts[Math.floor(Math.random() * facts.length)];
      const handle = selected.handle.replace(/^@/, "");

      quote.textContent = selected.fact;
      authorName.textContent = selected.name;
      authorHandle.textContent = selected.handle;
      authorHandle.href = "https://bsky.app/profile/" + encodeURIComponent(handle);
      card.hidden = false;
    })
    .catch(function (error) {
      quote.textContent = error.message;
      authorName.textContent = "";
      authorHandle.textContent = "";
      card.hidden = false;
    });
})();

