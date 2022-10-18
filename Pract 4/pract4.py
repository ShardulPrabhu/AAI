def conditional():
    pas_stats = 0.15
    pass_codingWstats = 0.60
    pass_codingWOstats = 0.40
    prob_both = pas_stats * pass_codingWstats
    print("the probability that applicant passes both is:",round(prob_both,3))
    prob_coding = (prob_both)+((1-pas_stats)*pass_codingWOstats)
    print("The probability that he/she passes only coding is:",round(prob_coding, 3))
    stats_given_coding = prob_both/prob_coding
    print("Conditional Probability is:",round(stats_given_coding,3))

print("Name: Shardul Prabhu")
conditional()
