/* For switching content */
url = "";

function page(page) {
  switch (page) {
    case "radio":
      url = "Radiopaedia/data.json";
      break;
    case "wiki":
      url = "Wikimedia/data.json";
      break;
    case "kaggle":
      url = "Kaggle/data.json";
      break;
  }

  $.ajax({
    url: url,
    dataType: "json",
    type: "get",
    cache: false,
    success: function (data) {
      document.getElementsByClassName("images")[0].remove();
      let content = document.createElement("div");
      content.className = "images";
      document.getElementById("main").appendChild(content);
      $(data).each(function (index, value) {
        let card = document.createElement("div");
        card.className = "data";
        card.innerHTML = `<div class="img"><img src="${value.link}"></div>
                        <div class="label">${value.title}</div>`;
        document.getElementsByClassName("images")[0].appendChild(card);
      });
    },
  });
}

/* display first page */
page("kaggle");