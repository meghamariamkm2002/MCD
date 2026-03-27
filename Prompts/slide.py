def prompt_par_slide(par_group):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image (S) <image>  

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

    Paper Segment: 
        [
        {{
            "para_id": "p3",
            "section_heading": "1 Introduction",
            "text": "Interactions among features can significantly improve the model’s expression capability. For a simple example, by incorporating the two-way interaction effect between gender (0/1: female and male) and age into the linear regression model height ∼ w1 · gender + w2 · age+ w3 · gender × age+ w0 (where w0, w1, w2, w3 are trainable parameters), the effects of female’s age on the heights will be different from that of male (w2 v.s. w2+w3). A predictive model f(x) has a k-way interaction effect if it satisfies [9]:",
            "seg_type": "par"
        }},
        {{
            "para_id": "p28",
            "section_heading": "2 Motivation - Reinterpreting ReLU-based DNN",
            "text": "We observe that a polyhedron ∆ is defined using a sequence of hyperplanes corresponding to the affine functions in different layers, but the attention of ReLU-activated DNNs is calculated based only on the hyperplane in the last layer for the polyhedron (piece). Although not all of the hyperplanes in early layers make the active boundary of a polyhedron (i.e., the polyhedron can locate in the interior of a half-space), using only one hyperplane in the attention is restrictive. An attention mechanism that allows multiple active boundary hyperplanes of a polyhedron to aid attention calculation may increase the model’s expression power. Let H∆ contain all of the active boundary hyperplanes H of ∆. For convenient notation, and with mild relaxation, we rescale the WH to −WH for those inactivated affine functions in the DNN so the half-spaces can all be written in the form of WHx + bH ≥ 0. Then, 1(x ∈ ∆) = ∏ H∈H∆ 1(WHx+bH ≥ 0). To learn feature interaction effects, we multiply the distances from x to each hyperplane in H∆. Given a hyperplane is linear in terms of x, multiplying the distances from x to two (m) hyperplanes creates quadratic (m-th order) terms. Thus, the number of active boundary hyperplanes of ∆ offers the upper bound on the order of the multiplicative terms",
            "seg_type": "par"
        }},
        {{
            "para_id": "p34",
            "section_heading": "3 The Proposed Polyhedron Attention Module (PAM)",
            "text": "functions to be affine functions, so θ contains the normal vector W and offset b. Sec 3.2 explains why affine functions are our choice. Instead of forming polyhedrons by intersecting hyperplanes as done in ReLU-activated DNNs, we use a tree search to partition the input space into overlapping polyhedrons. Note that the potential set of partitions created by tree search is a superset of that created by hyperplance intersections (see Appendix B). We introduce how we generate polyhedrons and then discuss the attention and value functions.",
            "seg_type": "par"
        }},
        {{
            "para_id": "p36",
            "section_heading": "3.1 Generating polyhedrons via oblique tree",
            "text": "where Un indicates the width of the overlapping buffer. Eq. 5 shows that those instances satisfying |Wnx+ bn| < Un belong to the buffer in both ∆nL and ∆nR . This buffer creates a symmetric band around the splitting hyperplane.",
            "seg_type": "par"
        }}
        ]
    Output:
    {{
        "results": {{
            "p3": 0.97,
            "p28": 0.24,
            "p34": 0.23,
            "p36": 0.12
        }},
        "explanation": "Paragraph p3 aligns closely with the slide content explaining interaction effects using the age–gender example, so it receives a high score. Paragraphs p28, p34, and p36 do not match the slide content and discuss unrelated technical details, resulting in low relevance scores."
    }}


    Example 2:
    Input:
    Slide Segment: <image>

    Paper Segments:
    [
        {{
            "para_id": "p4",
            "section_heading": "1 Introduction",
            "text": "Online convex optimization (OCO) is a versatile model that depicts the interaction between a learner and the environments over time [Hazan, 2016, Orabona, 2019]. In each round t ∈ [T ], the learner selects a decision xt from a convex compact set X ⊆ Rd, and simultaneously the environments choose a convex loss function ft : X 7→ R. Subsequently, the learner incurs a loss ft(xt), obtains information about the online function, and updates the decision to xt+1, aiming to optimize the game-theoretical performance measure known as regret [Cesa-Bianchi and Lugosi, 2006]:",
            "seg_type": "par"
        }},
        {{
            "para_id": "p6",
            "section_heading": "1 Introduction",
            "text": "In OCO, the type and curvature of online functions significantly impact the minimax regret bounds. Specifically, for convex functions, online gradient descent (OGD) can achieve an O( √ T ) regret guarantee [Zinkevich, 2003]. For α-exp-concave functions, online Newton step (ONS), with prior knowledge of the curvature coefficient α, attains an O(d log T ) regret [Hazan et al., 2007]. For λ-strongly convex functions, OGD with prior knowledge of the curvature coefficient λ and a different parameter configuration enjoys an O(log T ) regret [Hazan et al., 2007]. Note that the above",
            "seg_type": "par"
        }},
        {{
            "para_id": "p93",
            "section_heading": "A.2 Application II: Two-player Zero-sum Games",
            "text": "Theorem 4. Under Assumptions 1 and 2, for bilinear and strongly convex-concave games, the efficient version of Algorithm 1 enjoys O(1) regret summation in the honest case, O\u0302( \u221a T ) and O(log T )",
            "seg_type": "par"
        }},
    ]
    Output:
    {{
        "results": {{
            "p93": 0.95,
            "p6": 0.30,
            "p4": 0.25
        }},
        "explanation": "Paragraph p93 directly corresponds to the theorem described in the slide and is a fine-grain match, thus it receives a high relevance score. Paragraphs p6 and p4 discuss general concepts of Online Convex Optimization and regret bounds, which are related background material but not specific to the slide content, resulting in lower scores."
    }}



    Example 3:
    Slide Segment: <image>

    Paper Segments:
    [
        {{
            "para_id": "p19",
            "section_heading": "2 Preliminaries",
            "text": "omits logarithmic factors on leading terms. For example, Ô( √ V ) omits the dependence of log V .",
            "seg_type": "par"
        }},
        {{
            "para_id": "p20",
            "section_heading": "2 Preliminaries",
            "text": "Assumption 1 (Boundedness). For any x,y ∈ X and t ∈ [T ], the domain diameter satisfies ∥x − y∥ ≤ D, and the gradient norm of the online functions is bounded by ∥∇ft(x)∥ ≤ G. Assumption 2 (Smoothness). All online functions are L-smooth: ∥∇ft(x)−∇ft(y)∥ ≤ L∥x−y∥ for any x,y ∈ X and t ∈ [T ].",
            "seg_type": "par"
        }},
        {{
            "para_id": "p21",
            "section_heading": "2 Preliminaries",
            "text": "Both assumptions are common in the literature. Specifically, the boundedness assumption is common in OCO [Hazan, 2016]. The smoothness assumption is essential for first-order algorithms to",
            "seg_type": "par"
        }}
    ]

    Output:
    {{
        "results": {{
            "p19": 0.32,
            "p20": 0.31,
            "p21": 0.30
        }},
        "explanation": "All paragraphs (p19, p20, p21) describe theoretical assumptions or definitions from the preliminaries section, whereas the slide is a summary slide presenting key results. Therefore, none of these paragraphs provide a fine-grain match, resulting in uniformly low relevance scores."
    }}

    Provide a score for all input paper segment(paragraphs); do not skip any.
    """

    return prompt

def prompt_figure_slide(caption_figure, fig_id):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image <image>

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
    slide Segment: <image>

    Paper Segment: 
        Image: <image>
        Caption: Figure 4: Block-wise similarity attack. F\u03b1 is the image encoder, and F\u03b2 is the Transformer encoder.
        Fig_id: sp_2020_005
    Output:
    {{
        "result": {{'sp_2020_005': 0.9977}}
        "explanation": "Both the paper segment and the slide discusses the same thing. Look into the title of the slide."
    }}

    Provide a score for all input paper segment(figure segment); do not skip any.
    """

    return prompt


def prompt_algo_slide(cand_algo_text, algo_id):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query:  Slide image <image>

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
    Slide Segment:
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

def prompt_eq_slide(all_eqns):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Slide image <image>

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