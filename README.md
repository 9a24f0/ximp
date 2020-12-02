# ximp
`ximp` is abbreviation of "X-ray Image Monitoring Project"

The project focuses on X-ray Image of [Pneumonia](https://en.wikipedia.org/wiki/Pneumonia).

Here is the structure of the project
```
.
├── LICENSE
├── Kaggle
│   ├── img
│   ├── pre_process.py
│   └── data.json
├── Radiopaedia
│   ├── data.json
│   └── radio.py
├── README.md
└── Wikimedia
    ├── data.json
    └── scraper.py
```

Each folder has a file to scrape the data from web source and a json file to store all the link to the images.

We also visualized the data on [GitHub Pages](https://9a24f0.github.io/ximp/), please check branch [gh-pages](https://github.com/9a24f0/ximp/tree/gh-pages) for the code of the visualization.