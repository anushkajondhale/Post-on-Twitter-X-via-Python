# Post on Twitter (X) via Python

This project demonstrates how to create a **Twitter (X) post using Python** and the Twitter API v2.

## ⚙️ Setup
1. Install dependencies:
   ```bash
   pip install requests
````

2. Update `env.example.txt` with your Twitter Bearer Token.

   * Generate one from the Twitter Developer Portal.

3. Load environment variables:

   ```bash
   source load_env.sh
   ```

4. Run the script:

   ```bash
   python3 post_twitter.py
   ```

## 📌 Notes

* The script posts a simple text tweet.
* Extend it to post images, videos, or reply to threads.



