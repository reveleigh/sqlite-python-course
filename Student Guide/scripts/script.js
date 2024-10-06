const redactedSpans = document.querySelectorAll(".redacted");

redactedSpans.forEach((span) => {
  span.addEventListener("click", () => {
    span.classList.toggle("unredacted");
  });
});
