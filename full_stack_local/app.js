const form = document.querySelector("#case-form");
const inputText = document.querySelector("#input-text");
const outputText = document.querySelector("#output-text");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  outputText.value = "Working...";

  const formData = new FormData();
  formData.append("text", inputText.value);

  try {
    const response = await fetch("/cgi-bin/reverse_case.py", {
      method: "POST",
      body: new URLSearchParams(formData),
    });

    outputText.value = await response.text();
  } catch (error) {
    outputText.value = "Something went wrong. Is the local server running?";
  }
});
