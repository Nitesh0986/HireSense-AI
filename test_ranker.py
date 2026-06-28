from utils.ranker import rank_candidates

candidate_scores = [

    {
        "name": "Rahul.pdf",
        "score": 91.2
    },

    {
        "name": "Nitesh.pdf",
        "score": 83.4
    },

    {
        "name": "Amit.pdf",
        "score": 76.5
    }

]

ranked = rank_candidates(candidate_scores)

print("=" * 50)
print("Candidate Ranking")
print("=" * 50)

for index, candidate in enumerate(ranked, start=1):

    print(
        f"{index}. {candidate['name']} -> {candidate['score']}%"
    )