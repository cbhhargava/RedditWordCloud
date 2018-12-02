import oauth, fetch, word_cloud

red = oauth.get_connection()
tok = fetch.get_corpus(red, "https://www.reddit.com/r/DotA2/comments/a0m3m7/valve_heres_a_concept_design_for_a_new_learn_tab/")
word_cloud.generate_cloud(tok)
