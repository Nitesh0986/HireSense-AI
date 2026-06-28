def rank_candidates(candidate_list):
    """
    Sort candidates according to ATS score.
    """

    ranked = sorted(
        candidate_list,
        key=lambda x: x["ATS Score"],
        reverse=True
    )

    return ranked