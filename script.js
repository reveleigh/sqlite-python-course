const headers = document.querySelectorAll(".accordion-header");

headers.forEach((header) => {
  header.addEventListener("click", () => {
    const content = header.nextElementSibling;
    const icon = header.querySelector(".icon");

    // Toggle the 'open' class
    content.classList.toggle("open");

    // Calculate the height of the content
    const contentHeight = content.scrollHeight;

    // Set the max-height based on the 'open' state
    content.style.maxHeight = content.classList.contains("open")
      ? `${contentHeight}px`
      : "0px";

    // Change the icon
    icon.textContent = content.classList.contains("open") ? "-" : "+";
  });
});
