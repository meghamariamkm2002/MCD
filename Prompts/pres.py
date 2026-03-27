def prompt_par_pres(transcript, par_group):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image (S) <image>  Transcript: {transcript}

    Candidate: 
    Paper Paragraphs: {par_group}

    Instructions:
    Determine how relevant each paper segment is to the video segment.
    If relevant, briefly explain why.
    If not relevant, state that it is not relevant and explain why.
    There must be a direct, fine-grained overlap between the video content and the equation.
    Only assign a high score if most of the concepts mentioned in the video appear explicitly in the equation.
    When giving the relevance score consider the paper segment in isolation (do not compare it with others).

    Output Format (strict JSON):
    {{
        "results": {{"<paper_segment_id_1>": <float_between_0_and_1>, "<paper_segment_id_2>": <float_between_0_and_1>, ...}},
        "explanation": "<few lines summarizing reasoning for the assigned scores>"
    }}

    Example 1:
    Input:
    Slide Segment: <image>
    Transcript: 
    And we show that over these various search spaces and experiments, our method and app for neural acquisition process outperforms all the baselines.

    Paper Segment: 
        [
        {{
                "para_id": "p50",
                "section_heading": "4.2 Sequence Optimisation Experiments",
                "text": "Now, we demonstrate NAP’s abilities beyond hyperparameter tuning tasks in two real-world combinatorial black-box optimisation problems.",
                "seg_type": "par"
            }},
            {{
                "para_id": "p51",
                "section_heading": "4.2 Sequence Optimisation Experiments",
                "text": "Antibody CDRH3-Sequence Optimisation This experiment focuses on finding antibodies that can bind to target antigens. Antigens are proteins, i.e., sequences of amino acids that fold into a 3D shape giving them specific chemical properties. A protein region called CDRH3 is decisive in the antibody’s ability to bind to a target antigen. Following the work in [47], we represent CDRH3s as a string of 11 characters, each character being the code for a different amino acid in an alphabet of cardinality 22. The goal is to find the optimal CDRH3 that minimises the binding energy towards a specific antigen. Binding energies can be computed using state-of-the-art simulation software like Absolut! [48]. We collected datasets of CDRH3 sequences and their respective binding energies (with Absolut!) across various antigens from the protein database bank [49]. We then formed a transfer scenario across antigens where we meta-learn on 109 datasets, validate on 16, and test NAP on 32 new antigens. Our results in Figure 2 indicate that NAP is not limited to hyperparameter tuning tasks but can also outperform all other baselines in combinatorial domains.",
                "seg_type": "par"
            }},
            {{
                "para_id": "p52",
                "section_heading": "4.2 Sequence Optimisation Experiments",
                "text": "Electronic Design Automation (EDA) Logic synthesis (LS) is an essential step in the EDA pipeline of the chip design process. At the beginning of LS, we represent the circuit as an AIG (an And-InverterGraph representation of Boolean functions) and seek to map it to a netlist of technology-dependent gates (e.g., 6-input logic gates in FPGA mapping). The goal in LS is to find a sequence of graph transformations such that the resulting netlist meets an objective that trades off the number of gates (area) and the size of the longest directed path (delay) in the netlist. We perform a sequence of logic synthesis operators dubbed a synthesis flow to optimise the AIG.",
                "seg_type": "par"
            }},
            {{
                "para_id": "p53",
                "section_heading": "4.2 Sequence Optimisation Experiments",
                "text": "Following [50], we consider length 20 LS flows and allow an alphabet of 11 such operators, e.g., {{refactor, resub, . . . , balance}} as implemented in the open-source ABC library [51]. We collected datasets for 43 different circuits. Each dataset consisted of 500 sequences (collected via a Genetic algorithm optimizer) and their associated area and delay. Additionally, we applied the well-known heuristic sequence resyn2 on each circuit to get a reference area and delay. For this task, the black-box takes a sequence as input and returns the sum of area and delay ratios with respect to the reference ones, as detailed in Appendix B.1. We train all methods on 30 circuits from OpenABC [50], validate on 4 and test on 9. Our results in Figure 2 again demonstrate that NAP outperforms all other baselines by a significant margin.",
                "seg_type": "par"
            }},
        ]
    Output:
    {{
    "results": {{
        "p50": 0.3,
        "p51": 0.9,
        "p52": 0.8,
        "p53": 0.85
    }},
    "explanation": "Paragraphs p51–p53 are strongly relevant since they describe the experimental results and show NAP outperforming baselines, which matches the transcript content. Paragraph p50 provides only general context, so it receives a lower score."
    }}



    Example 2:
    Input:
    Slide Segment: <image>
    Transcript:
    And we show that over these various search spaces and experiments, our method and app for neural acquisition process outperforms all the baselines.
    Paper Segments:
    [
        {{
            "para_id": "p28",
            "section_heading": "3.2 Limitations of Regret Rewards in End-to-End Training",
            "text": "To define Equation 1, we followed the well-established literature of meta-BO [4, 13] and utilised simple regret reward functions. Although this choice is reasonable, we face challenges in applying such rewards in end-to-end training. Apart from difficulties associated with end-to-end training",
            "seg_type": "par"
        }},
        {{
            "para_id": "p29",
            "section_heading": "3.2 Limitations of Regret Rewards in End-to-End Training",
            "text": "of deep architectures [18], our RL algorithm is subject to additional complexities when estimating gradients from Equation 1 due to the sparsity of the reward function. To better understand this problem, we start by noticing that for a reward component r(k)t to contribute to the cumulative summation ∑ t γ t−1r (k) t , we need to observe a function value y (k) t that outperforms all values we have seen so far, i.e., y(k)t > max1≤ℓ<t y (k) ℓ . During the early training stages of RL, we can quantify the average number of such informative events (when y(k)t > max1≤ℓ<t y (k) ℓ ) by a combinatorial argument that frames this calculation as a calculation of the number of cycles in a permutation of T (k) elements, leading us to the following lemma. Lemma 3.1. Consider a task with a horizon length (budget) T , and define rt = max1≤ℓ≤t yt the simple regret as introduced in Equation 1. For a history HT , let mH denote the total number of informative rewards, i.e. the number of steps t at which yt > max1≤ℓ<t yℓ. Under a random policy πθ, the number of informative events is logarithmic in T such that: EH∼pπθ [mH] = O (log T ), where pπθ is induced by πθ as in Equation 2.",
            "seg_type": "par"
        }},
        {{
            "para_id": "p30",
            "section_heading": "3.2 Limitations of Regret Rewards in End-to-End Training",
            "text": "We defer the proof of Lemma 3.1 to Appendix A due to space constraints. Here, we note that this result implies that the information contained in one sampled trajectory is sparse at the beginning of RL training when the policy acts randomly. Of course, this increases the difficulty of estimating informative gradients of Equation 1 when updating θ. One can argue that the sparsity described in Lemma 3.1 only holds under random policies during the early stages of RL training and that sparsity patterns decrease as policies improve. Interestingly, simple regret rewards do not necessarily confirm this intuition. To realise this, consider the other end of the RL training spectrum in which policies have improved to near optimality such that πθ → πθ⋆ . Because πθ has been trained to maximise regret, it will seek to suggest the optimal point of the current task, as early as possible in the BO trajectory. Consequently, the policy is encouraged to produce trajectories with even sparser rewards during later training stages, further complicating the problem of informative gradient estimates of Equation 1.",
            "seg_type": "par"
        }},
        {{
            "para_id": "p31",
            "section_heading": "3.3 Inductive Biases and Auxiliary Tasks",
            "text": "Learning from sparse reward signals is a well-known difficulty in the reinforcement learning literature [32]. Many solutions, from imitation learning, [35] to exploration bonuses [36], improve reward signals to reduce agent-environment interactions and enhance gradient updates. Others [37] attempt to define more informative rewards from prior knowledge or via human interactions [38]. Unfortunately, both of those approaches are hard to use in BO. Indeed, manually engineering black-box-specific rewards is notoriously difficult and requires domain expertise and extensive knowledge of the source and target black-box functions we wish to optimise. Furthermore, learning from human feedback is data-intensive, conflicting with the goal of sample-efficient optimisation.",
            "seg_type": "par"
        }}
    ]
    Output:
    {{
    "results": {{
        "p28": 0.1,
        "p29": 0.1,
        "p30": 0.1,
        "p31": 0.05
    }},
    "explanation": "The transcript and slide(shows figure illustrating performance) focuses on experimental performance comparisons, while paragraphs p28–p30 discuss theoretical limitations of regret-based rewards and p31 introduces inductive biases and auxiliary tasks. None directly address outperforming baselines, so all receive low relevance scores."
    }}

    Provide a score for all input paper segment(paragraphs); do not skip any.
    """

    return prompt

def prompt_figure_pres(transcript, caption_figure, fig_id):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image (S) <image>  Transcript: {transcript}

    Candidate: 
    Paper Segment: consists of a figure & caption: <image>
    Caption: {caption_figure}
    Fig_id: {fig_id}

    Instructions:
    Determine how relevant each paper segment is to the video segment.
    If relevant, briefly explain why.
    If not relevant, state that it is not relevant and explain why.
    There must be a direct, fine-grained overlap between the video content and the equation.
    Only assign a high score if most of the concepts mentioned in the video appear explicitly in the equation.
    When giving the relevance score consider the paper segment in isolation (do not compare it with others).

    Output Format (strict JSON):
    {{
        "results": {{"<paper_segment_id_1>": <float_between_0_and_1>, "<paper_segment_id_2>": <float_between_0_and_1>, ...}},
        "explanation": "<few lines summarizing reasoning for the assigned scores>"
    }}

    Example 1:
    Input:
    Video Segment: <image>
    Transcript: To solve this task, we propose VL attack.
    The overall structure is shown on the slide.
    Here the VL attack consists of two parts.
    The first is the single model level attack, where we use a from image text attack order as the firmware can be perturbed on continuous space.
    We will later introduce the details of the BSA in the block-wise similarity attack.
    If the image attack fails, we move to a text attack using the bridge attack method.
    If both single-model attack fails, we move to the multi-model level attack, where we iteratively cross-search the combination between the image perturbation and the text perturbation.

    Paper Segment: 
        Image: <image>
        Caption: Figure 4: Block-wise similarity attack. F\u03b1 is the image encoder, and F\u03b2 is the Transformer encoder.
        Fig_id: sp_2020_005
    Output:
    {{
        "result": {{'sp_2020_005': 0.9977}}
        "explanation": "The exact figure is shown in the slide"
    }}

    Provide a score for all input paper segment(figure segment); do not skip any.
    """

    return prompt


def prompt_algo_pres(transcript, cand_algo_text, algo_id):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image (S) <image>  Transcript: {transcript}

    Candidate: 
    Paper Segment: consists of an algorithm:
    {cand_algo_text}
    Algo_id: {algo_id}

    Instructions:
    Determine how relevant each paper segment is to the video segment.
    If relevant, briefly explain why.
    If not relevant, state that it is not relevant and explain why.
    There must be a direct, fine-grained overlap between the video content and the equation.
    Only assign a high score if most of the concepts mentioned in the video appear explicitly in the equation.
    When giving the relevance score consider the paper segment in isolation (do not compare it with others).

    Output Format (strict JSON):
    {{
        "results": {{"<paper_segment_id_1>": <float_between_0_and_1>, "<paper_segment_id_2>": <float_between_0_and_1>, ...}},
        "explanation": "<few lines summarizing reasoning for the assigned scores>"
    }}

    Example 1:
    Video Segment:
    Transcript: Similarly, for TCCO, we maintain MSVRS meters for both inner functions, G and H, and update the parameter W using SGD as well.
    Slide image: <image>

    Paper Segment:
    Algorithm: Igorithm 2 Stochastic Optimization algorithm for Non-smooth TCCO (SONT)\n1: Initialization: w0, {{ui,0 : i  S1}}, vi,j,0 = hi,j(w0; B0,i,j) for all (i, j)  S1 \u00d7 S2.\n2: for t = 0, . . . , T \u2212 1 do\n3:\nSample batches Bt  S1, Bt  S2, and Bt,i,j  Di,j for i  Bt and j  Bt2.\n(\u03a0h [(1 \u2212 \u03c41)vi,j,t + \u03c41hi,j (wt; Bt,i,j) + \u03b31(hi,j (wt; Bt,i,j) \u2212 hi,j(wt\u22121; Bt\n1:\nvi,j,t+1 =\n(i, j)  Bt x Bt\nVi,j,t,\n(i, j) \u03be Bt \u00d7 Bt\n\u222b (1 \u2212 \u03c42)ui,t + 12 \u2211 jBt [\u03c42gi(vi,j,t) + \u03b32(gi(vi,t) \u2212 gi(vi,j,t\u22121)], i  Bt\n:\nUi,t+1\n=\nui,t, i & Bt\nGt = B1 \u2211iBt (B1 \u2211iBz hi,j(wt; B3,i,j)\u2202gi(vi,t) \u2202fi(ui,t]\nUpdate wt+1 = wt \u2212 \u03b7Gt
    Algo_id: sp_2036_page_6_1
    Output: 
    {{
        "result": {{'sp_2036_page_6_1': 0.9891}},
        "explanation": "The algorithm in slide and paper segment is same. Hence very high relevance score."
    }}

    Provide a score for all input paper segment(algorithm); do not skip any.
    """

    return prompt

def prompt_eq_pres(transcript, all_eqns):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image (S) <image>  Transcript: {transcript}

    Candidate: 
    Paper Segment: Equations:
    {all_eqns}

    Instructions:
    Determine how relevant each paper segment is to the video segment.
    If relevant, briefly explain why.
    If not relevant, state that it is not relevant and explain why.
    There must be a direct, fine-grained overlap between the video content and the equation.
    Only assign a high score if most of the concepts mentioned in the video appear explicitly in the equation.
    When giving the relevance score consider the paper segment in isolation (do not compare it with others).

    Output Format (strict JSON):
    {{
        "results": {{"<paper_segment_id_1>": <float_between_0_and_1>, "<paper_segment_id_2>": <float_between_0_and_1>, ...}},
        "explanation": "<few lines summarizing reasoning for the assigned scores>"
    }}

    Example 1:
    Input:
    Slide Segment: <image>
    Transcript: 
            Now we show an application.
            In two-way partial ALC maximization, we restrict the false positive rate by an upper bound and the true positive rate by a lower bound.
            It will result in a coupled compositional problem with non-smooth outer and inner functions, which can be solved by the proposed method.

    Paper Segment:
    {{
        {{
            "box": [
                343.7732849121094,
                170.27809143066406,
                877.39697265625,
                222.0182647705078
            ],
            "text": [
                "\\\\underset{{\\\\mathbf{{w}}}}{{\\\\operatorname*{{min}}}}\\\\;\\\\frac{{1}}{{n_{{+}}}}\\\\frac{{1}}{{n_{{-}}}}\\\\sum_{{X_i \\\\in \\\\mathcal{{S}}_{{+}}^{{\\\\dagger}}[1, k_{{1}}]}}\\\\sum_{{X_j \\\\in \\\\mathcal{{S}}_{{-}}^{{\\\\pm}}[1, k_{{2}}]}}\\\\ell\\\\!\\\\left(h_{{\\\\mathbf{{w}}}}(X_{{j}}) - h_{{\\\\mathbf{{w}}}}(X_{{i}})\\\\right),"
            ],
            "page": "sp_2036_page_0008",
            "id": "sp_2036_page_0008-1",
            "seg_type": "eq"
        }},
        {{
            "box": [
                425.4681396484375,
                237.79095458984375,
                794.6944580078125,
                264.38800048828125
            ],
            "text": [
                "\\\\forall i \\\\in [ 1 , \\\\ldots , N ] : \\\\mathbf{{a}}_{{i}} = \\\\mathbf{{W}}_{{i}} \\\\mathbf{{h}}_{{i - 1}}, \\\\mathbf{{h}}_{{i}} = f_{{i}}(\\\\mathbf{{a}}_{{i}})."
            ],
            "id": "sp_0001_page_0003-3",
            "page": "sp_0001_page_0003",
            "seg_type": "eq"
        }}
    }}
    Output:
    {{
        'result': {{"sp_2036_page_0008": 0.9877, "sp_0001_page_0003-3":0.1}},
        "explanation": "sp_2036_page_0008 is related with slide but sp_0001_page_0003-3 is not."
    }}

    Provide a score for all input paper segment(equations); do not skip any.
    """

    return prompt