def prompt_par_exp(transcript, par_group):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Transcript - {transcript}

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
    Video Segment: Hi there.
    Today we'll look at Direct Feedback Alignment, Scales to Modern Deep Learning Tasks and Architectures by Julia Lone, Jacopo Poli, François Boniface, and Florin Krizakala.
    So this paper, on a high level, it replaces the back propagation algorithm in deep learning architectures with this algorithm called Direct Feedback Alignment, which is more biologically plausible.
    The algorithm has been around for a while, but it hasn't yet been shown to be applicable to really modern big deep learning architectures and then perform on par with backprop on modern deep learning tasks.
    This paper, as I understand it, is the first one to demonstrate that it can do that.
    So this is very much an engineering paper, an applied paper, and
    We're going to mostly go into direct feedback alignment as such, and I don't think we're going to go too much into what the actual empirical findings are, because even though they're impressive and it's a good piece of engineering, I think they can be summarized pretty much by, it works not yet on par with back propagation, but into a promising direction.
    Alright, as always, if you like content like this, consider sharing it out and leaving a like and tell me in the comments what you like.
    Of course, subscribe if you aren't yet.
    That is, you know, essential.
    Otherwise, how are we going to hear from me in the future?
    Okay, let's dive in.
    They say, despite being the

    Paper Segment: 
        [
        {{
            par_id: p12
            text: Despite being the workhorse of deep learning, the backpropagation algorithm is 
        no panacea. It enforces sequential layer updates, thus preventing efﬁcient paral- 
        lelization of the training process. Furthermore, its biological plausibility is being 
        challenged. Alternative schemes have been devised; yet, under the constraint of 
        synaptic asymmetry, none have scaled to modern deep learning tasks and architec- 
        tures. Here, we challenge this perspective, and study the applicability of Direct 
        Feedback Alignment (DFA) to neural view synthesis, recommender systems, geo- 
        metric learning, and natural language processing. In contrast with previous studies 
        limited to computer vision tasks, our ﬁndings show that it successfully trains a large 
        range of state-of-the-art deep learning architectures, with performance close to 
        ﬁne-tuned backpropagation. When a larger gap between DFA and backpropagation 
        exists, like in Transformers, we attribute this to a need to rethink common practices 
        for large and complex architectures. At variance with common beliefs, our work 
        supports that challenging tasks can be tackled in the absence of weight transport.
        }},
        {{
            par_id: p13
            text: Consequently, alternative training algorithms have been developed. Some of these algorithms are 
            explicitly biologically inspired [7–13], while others focus on making better use of available compute 
            resources [3, 14–19]. Despite these enticing characteristics, none has been widely adopted, as they 
            are often demonstrated on a limited set of tasks. Moreover, as assessed in [20], their performance on 
            challenging datasets under the constraint of synaptic asymmetry is disappointing.
        }},
        {{
            par_id: p14
            text: While the backpropagation algorithm (BP) [1, 2] is at the heart of modern deep learning achievements, 
            it is not without pitfalls. For one, its weight updates are non-local and rely on upstream layers. Thus, 
            they cannot be easily parallelized [3], incurring important memory and compute costs. Moreover, 
            its biological implementation is problematic [4, 5]. For instance, BP relies on the transpose of the 
            weights to evaluate updates. Hence, synaptic symmetry is required between the forward and backward 
            path: this is implausible in biological brains, and known as the weight transport problem [6]
        }},
        {{
            par_id: p15
            text: We seek to broaden this perspective, and demonstrate the applicability of Direct Feedback Alignment 
            (DFA) [19] in state-of-the-art settings: from applications of fully connected networks such as neural 
            view synthesis and recommender systems, to geometric learning with graph convolutions, and natural 
            language processing with Transformers. Our results deﬁne new standards for learning without weight 
            transport and show that challenging tasks can indeed be tackled under synaptic asymmetry.
        }},
        ]
    Output:
    {{
    "results": {{"p12": 0.95, "p13": 0.40, "p14": 0.30, "p15": 0.90}},
    "explanation": "Paragraphs p12 and p15 directly describe Direct Feedback Alignment (DFA) as a scalable and biologically plausible alternative to backpropagation, matching the video discussion. Paragraphs p13 and p14 mention alternative algorithms or backpropagation limitations without focusing on DFA’s scalability, making them less relevant."
    }}
    Example 2:
    Input:
    Video Segment: the point will be closer to one of them than to the other.
    And that's how we evaluate similarity.
    Now, what does this path have to do with this?
    So as I said here, we've simply chosen a model, right?
    We can, we don't have to do this for the final model.
    We can do this for any model.
    And in fact, what we're going to do is if we have a new data point,
    So remember that our model evolved from this down here to this.
    If we have a new data point, we're going to rewind time and start out at the beginning with the first model
    do this measurement, like compare our data point to all the other data points for this model, then we're going to advance one step and we're going to do it again and advance one step and we're going to do it again.
    And we're going to consider the similarity scores over as an average over that path.
    So that means in order to classify a data point in this view, as I said, this is not a practical algorithm.
    In order to classify our data point, we're going to retrace the path of weights that the model took during gradient descent when it was learned.
    We're going to retrace that along the path.
    And for each step in the path, we're going to compare our data points effect on the neural network.
    So the neural network's sensitivity to our data point.
    and we're going to compare that with the neural network's sensitivity to all the data points in our training example.
    And then we're going to classify our data point by whichever data points in the training example had a similar effect on the neural network over the course of training.
    So we're not going to train the network more or anything.
    We're simply going to replay the path we took during radiant descent and by looking at how the data points affect the network during that path in terms of their gradients, like how much they pull on the network, even though we're not going to do the steps.
    By those polls, we classify how if two data points are similar or not.

    Paper Segments:
    [
        {{
            "para_id": "p37",
            "section_heading": "3.2 Geometric Learning with Graph Convolutional Networks",
            "seg_type": "par",
            "text": "Results We report classification accuracy in Table 3. BP and DFA regularization and optimization hyperparameters are fine-tuned separately on the Cora dataset. In general, we find that less regularization and lower learning rates are needed with DFA. DFA successfully trains all graph methods, independent of whether they use the spectral domain or not, and even if they use attention. Furthermore, for GraphConv, SplineConv, and GATConv DFA performance nearly matches BP.",
        }},
        {{
            "para_id": "p46",
            "section_heading": "3.3 Natural Language Processing with Transformers",
            "seg_type": "par",
            "text": "Results Our results are summarized in Table 5. Hyper-parameters fine-tuned for BP did not fare well with DFA, but changes in the optimizer narrowed the gap between BP and DFA considerably. The learning rate schedule used on top of Adam [83] in [63] proved detrimental. Using Adam alone required reducing the learning rate between BP and DFA. Increasing β2 from 0.98 [63] to 0.999 improved performance significantly. Finally, a simple scheduler that reduces the learning rate when the validation perplexity plateaus helped reducing it further. Considering that the perplexity of the shallow baseline is over 400, DFA is clearly able to train Transformers. However, our results are not on par with BP, especially in the micro setting. A substantial amount of work remains to make DFA competitive with BP, even more so in a minimal weight transport scenario. The large performance improvements brought by small changes in the optimizer indicate that intensive fine-tuning, common in publications introducing state-of-the-art results, could close the gap between BP and DFA.",
        }},
        {{
            "para_id": "p47",
            "section_heading": "4 Conclusion and outlooks",
            "seg_type": "par",
            "text": "We conducted an extensive study demonstrating the ability of DFA to train modern architectures. We considered a broad selection of domains and tasks, with complex models featuring graph convolutions and attention. Our results on large networks like NeRF and Transformers are encouraging, suggesting that with further tuning, such leading architectures can be effectively trained with DFA. Future work on principled training with DFA–in particular regarding the influence of common practices and whether new procedures are required–will help close the gap with BP.",
        }},
        {{
            "para_id": "p48",
            "section_heading": "4 Conclusion and outlooks",
            "seg_type": "par",
            "text": "More broadly, we verified for the first time that learning under synaptic asymmetry is possible beyond fully-connected layers, and in tasks significantly more difficult than previously considered. This addresses a notable concern in biologically-plausible architectures. DFA still requires an implausible global feedback pathway; however, local training has already been demonstrated at scale. The next step towards biologically-compatible learning is a local method without weight transport."
        }},
        {{
            "para_id": "p49",
            "section_heading": "4 Conclusion and outlooks",
            "seg_type": "par",
            "text": "While the tasks and architectures we have considered are not biologically inspired, they constitute a good benchmark for behavioural realism [20]. Any learning algorithm claiming to approximate the brain should reproduce its ability to solve complex and unseen task. Furthermore, even though the current implementation of mechanisms like attention is devoid of biological considerations, they represent broader concepts applicable to human brains [84]. Understanding how our brain learns is a gradual process, and future research could incorporate further realistic elements, like spiking neurons.",
        }},
        {{
            "para_id": "p50",
            "section_heading": "4 Conclusion and outlooks",
            "seg_type": "par",
            "text": "Finally, unlocking the backward pass in large architectures like Transformers is promising. More optimized implementation of DFA–built at a lower-level of existing ML libraries–could unlock significant speed-up. Leveraging the use of a single random projection as the cornerstone of training, dedicated accelerators may employ more exotic hardware architectures. This will open new possibilities in the asynchronous training of massive models.",
        }},
    ]
    Output:
    {{
        "relevant_paragraphs": [],
        "non_relevant_paragraphs": [
            {{
                "results": {{"p37": 0.25, "p46": 0.20, "p47": 0.15, "p48": 0.10, "p49": 0.10, "p50": 0.05}},
                "explanation": "All paragraphs focus on experimental results or biological plausibility of DFA rather than on path-dependent similarity or retracing gradient descent dynamics discussed in the video. Hence, all have low relevance scores."
            }}
        ]
    }}


    Example 3:
    Input:
    Video Segment: That's how you come to conclude this proof.
    They have a lot of remarks right here.
    So they say this, for example, this differs from a typical kernel machines in that the AIs and Bs depend on X, which is something that's not, you know, the AIs and Bs are usually kind of learned, but here they are actually functions of X, which is a difference to classic kernel machines.
    Essentially, in order to make this a kernel machine, you have to have the train neural network already.
    It's not like this is a new training algorithm.
    It simply casts these models in the way of a kernel machine.
    In my mind, it's almost like it's a super general statement.
    It also connects it to boosting right here.
    I don't even know where but down here in the discussion it connects it to boosting and it just seems like at some point yet you can just connect all the learning algorithms to each other because all the learning algorithms
    will somehow incorporate the training data into their weights, like otherwise they wouldn't learn.
    And I feel like we're rediscovering just different methods of looking at problems.
    Now these different methods, the different way of looking at a problem can give rise to new and better algorithms because we understand the problem better
    But yeah, it's in some ways not a surprise.
    It's not a surprise that neural networks somehow store the training data because of course any learning algorithm must do so.
    And that's exactly what this paper shows.
    And it shows what the exact kernel is you have to choose in order to make that claim.
    solid.
    So that was the paper.
    I just want to read the most important point for this.
    Most significantly, however, learning path kernels, machines via gradient descent largely overcomes the scalability bottlenecks that have long limited the applicability of kernel methods to large data sets.
    computing and storing the gram matrix at learning time with its quadratic cost and the number of example is no longer required.
    So it makes a claim that if you want to build a kernel machine, you might as well, I don't actually know what that means.
    Does it mean you might as well find the neural network that is equivalent to the kernel you want to build?
    I don't know, if that just seems to turn out to mean that you should build the neural network that you like.
    But they kind of make the point that neural networks don't discover new representations, new features.
    What they actually do is they discover features of how you compare data points in this gradient space.
    And they do that by means of gradient descent.
    And the paper states that this is very, very dependent on how you choose the architecture.
    So by choosing the architecture of the neural network, you predispose the gradient descent algorithm to find certain features to compare data points as opposed to other features.
    And the paper again makes this explicit by showing how this comparison comes about, namely by means of the gradients with respect to the weights of the output of the neural network, which of course is entirely a function of both the architecture and the loss function and the dataset.
    All right, so I hope you've enjoyed this.
    Let me know what you think and I'll see you next time.
    Bye-bye.

    Paper Segments:
    [
        {{
            "para_id": "p31",
            "section_heading": "2. Path Kernels",
            "seg_type": "par",
            "text": "Remark 1 This differs from typical kernel machines in that the ai’s and b depend on x. Nevertheless, the ai’s play a role similar to the example weights in ordinary SVMs and the perceptron algorithm: examples that the loss is more sensitive to during learning have a higher weight. b is simply the prior model, and the final model is thus the sum of the prior model and the model learned by gradient descent, with the query point entering the latter only through kernels. Since Theorem 1 applies to every yi as a query throughout gradient descent, the training data points also enter the model only through kernels (initial model aside)."
        }},
        {{
            "para_id": "p43",
            "section_heading": "3. Discussion",
            "seg_type": "par",
            "text": "Most significantly, however, learning path kernel machines via gradient descent largely overcomes the scalability bottlenecks that have long limited the applicability of kernel methods to large data sets. Computing and storing the Gram matrix at learning time, with its quadratic cost in the number of examples, is no longer required. (The Gram matrix is the matrix of applications of the kernel to all pairs of training examples.) Separately storing and matching (a subset of) the training examples at query time is also no longer necessary, since they are effectively all stored and matched simultaneously via their superposition in the model parameters. The storage space and matching time are independent of the number of examples. (Interestingly, superposition has been hypothesized to play a key role in combatting the combinatorial explosion in visual cognition (Arathorn, 2002), and is also"
        }},
        {{
            "para_id": "p4",
            "section_heading": "1. Introduction",
            "seg_type": "par",
            "text": "Despite its many successes, deep learning remains poorly understood (Goodfellow et al., 2016). In contrast, kernel machines are based on a well-developed mathematical theory, but their empirical performance generally lags behind that of deep networks (Schölkopf and Smola, 2002). The standard algorithm for learning deep networks, and many other models, is gradient descent (Rumelhart et al., 1986). Here we show that every model learned by this method, regardless of architecture, is approximately equivalent to a kernel machine with a particular type of kernel. This kernel measures the similarity of the model at two data points in the neighborhood of the path taken by the model parameters during learning. Kernel machines store a subset of the training data points and match them to the query using the kernel. Deep network weights can thus be seen as a superposition of the training data points in the kernel’s feature space, enabling their efficient storage and matching. This contrasts with the standard view of deep learning as a method for discovering representations from data, with the attendant lack of interpretability (Bengio et al., 2013). Our result also has significant implications for boosting algorithms (Freund and Schapire, 1997), probabilistic graphical models (Koller and Friedman, 2009), and convex optimization (Boyd and Vandenberghe, 2004)."
        }}
    ]

    Output:
    {{
        "results": {{"p31": 0.95, "p43": 0.93, "p4": 0.90}},
        "explanation": "All three paragraphs correspond closely to the video discussion: p31 describes the difference from traditional kernel machines (ai’s and b depend on x), p43 discusses scalability via gradient descent and Gram matrix elimination, and p4 introduces the equivalence between deep networks and kernel machines."
    }}

    Provide a score for all input paper segment(paragraph); do not skip any.
    """

    return prompt



def prompt_fig_exp(transcript, caption_figure, fig_id):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Transcript - {transcript}

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
    Video Segment: 
    Transcript: Modulated by a random matrix.
        For example, look at one of them, this neural view synthesis with neural radiance fields.
        So neural radiance fields is a type of model to do this task of where you get a bunch of views of an object in 3D or, you know, a bunch of views around an object and you're supposed to render a new view.
        And you can see that the DFA parameter or the DFA updated nerve neural
        radiance field model is pretty close to the back propagation updated one.
        You can see it's a bit more blurry, but it works.
        And I think this paper is really trying to show that look this works.
        It doesn't work extremely well, but it works.
        And it works on a level that hasn't been seen before.
        So here, if you consider these results higher as better on the synthetic data set here, even you see that if you have the same model with back prop, it performs better than with DFA.
        But the DFA for that model performs better than these other baseline models that have themselves been trained with back propagation.
        So it's definitely in the direction of being competitive.
        you
        And that's the same thing they show with all of these experiments.
        So they apply this to graph networks.
        They apply this to transformers.
        And as I said, it's not there yet.
        You see that.
        So in the transformers, they have these settings where in macro, they just use it DFA for the individual blocks and micro, they use it for each layer and already told you that you still in the attention mechanism, you still have to use backprop within the attention mechanism.
        but it is much more of a plausible algorithm than the back propagation through the entire network.
        And they show that if they appropriately tweak the hyperparameters, they do get into the direction of something that's performant, at least with this macro strategy.
        Now, this is nowhere close to what the back propagation algorithm achieves.
        But it's sort of an indication that if the community could work as much on this as it has worked on back propagation, then probably we could push this to a place where it does perform on par with back prop or very close to it.
        So I do invite you to go and look at the experiments.
        They have a lot of lot of details on how they did it and exactly how you have to change the architectures to make DFA work and the hyper parameters and so on.
        So that's really cool.
        And they have some more outputs right here of the view synthesis and so on.
        Yeah.
        If you are interested in that thing, again, I don't want to disrespect it.
        I don't think there is much point in me going over it.
        The results are always sort of the same, that DFA, it's not there yet, but it's a good direction.
        I hope this was informative.
        Let me know if you disagree about my assessment of DFA.
        I could be completely wrong.
        Or this could be well known to people already.
        See you next time.


    Paper Segment: 
        Image: <image>
        Caption: Table 1: Peak Signal to Noise Ratio (PSNR, higher is better) of neural view synthesis methods trained with backpropagation against NeRF trained with DFA. Even when trained with DFA, NeRF outperforms two state-of-the-art methods on a synthetic dataset (NeRF-Synthetic), and achieves fair performance on a challenging real world views datasets (LLFF-Real). BP results from [39].
        Fig_id: sp_0001-Table1-1
    Output:
    {{
        "result": {{'sp_0001-Table1-1': 0.90}}
        "explanation": "The table and it's values are discussed in the talk, they do talk about the how values change for NeRF Synthetic from BP and DFA. This is hence a fine-grain match."
    }}
    

    Example 2:
    Input:

    Video Segment: 
    Transcript: Hi there.
        Today we'll look at Direct Feedback Alignment, Scales to Modern Deep Learning Tasks and Architectures by Julia Lone, Jacopo Poli, François Boniface, and Florin Krizakala.
        So this paper, on a high level, it replaces the back propagation algorithm in deep learning architectures with this algorithm called Direct Feedback Alignment, which is more biologically plausible.
        The algorithm has been around for a while, but it hasn't yet been shown to be applicable to really modern big deep learning architectures and then perform on par with backprop on modern deep learning tasks.
        This paper, as I understand it, is the first one to demonstrate that it can do that.
        So this is very much an engineering paper, an applied paper, and
        We're going to mostly go into direct feedback alignment as such, and I don't think we're going to go too much into what the actual empirical findings are, because even though they're impressive and it's a good piece of engineering, I think they can be summarized pretty much by, it works not yet on par with back propagation, but into a promising direction.
        Alright, as always, if you like content like this, consider sharing it out and leaving a like and tell me in the comments what you like.
        Of course, subscribe if you aren't yet.
        That is, you know, essential.
        Otherwise, how are we going to hear from me in the future?
        Okay, let's dive in.
        They say, despite being the

    
    Paper Segment: 
        Image: <image>
        Caption: Table 1: Peak Signal to Noise Ratio (PSNR, higher is better) of neural view synthesis methods trained with backpropagation against NeRF trained with DFA. Even when trained with DFA, NeRF outperforms two state-of-the-art methods on a synthetic dataset (NeRF-Synthetic), and achieves fair performance on a challenging real world views datasets (LLFF-Real). BP results from [39].
        Fig_id: sp_0001-Table1-1

    Output:
    {{
        "result": {{'sp_0001-Table1-1': 0.10}},
        "explanation": "The talk is introduces Direct Feedback Alignment (DFA) as a biologically plausible alternative to backpropagation and demonstrates its scalability to modern deep learning architectures.
        While not yet matching backprop’s performance, DFA shows promising results toward efficient, large-scale learning."
    }}

    Example 3:
    Input:
    Video Segment: 
    Transcript: is the thing here and they on this task on this metric learning tasks, they do outperform all other models right here.
        And what I find interesting is down here where they now test for the for the distribution shift.
        So
        What they're saying is, okay, this is all on data, basically, where we train on training data and evaluate on testing data.
        And they're sort of the same.
        They come from the same year, from the same machine translation models.
        And we don't really know how next year the machine translation models might be different.
        Thus, our scores still hold.
        So they try to simulate this by splitting the data and they introduce this skew factor.
        So what they'll do is they'll split the data.
        So usually, as you can see right here, the training date, the ratings, these are the human ratings, the training data is sort of distributed like
        This would be the test data and the training data would almost be overlapping that if you can see like the dotted lines right here or so.
        So you can see the overlap between the test and the trend of the human ratings is very close.
        Now they say we can we can skew that we can sort of filter the data such that in the training data
        Only very bad sentences are, and in the test data, there are only very good sentences.
        And this simulates the fact that this might be the previous year's data that we train our metric on, and then we evaluate it on the next year's data where all the systems have become better.
        And what this does is, you can see right here, the bottom axis is the test skew and the color here is the training skew.
        Okay, so what interests, what we're interested in is to the right and down the colors.
        So as these skew increases, you can see right here that the quality of the metric decreases, okay?
        The correlation with the human ratings decreases.
        But it still remains fairly well, but especially the training skew, if you update the train, so if you make the training examples really bad, so to say, the score just drops down.
        And they can show pretty well here that if you add this pre training, then the score, um, except in this extreme case, so the score for all of these, it remains relatively high and especially remains above the blue score, which is always sort of worse.
        Right.
        So this is, is pretty as pretty neat and shows this power of this pre training basically.
        That's the robustness to quality drift metric.
        They have a bunch of other metrics right here where they ablate and so on, but I don't want to go too much into that.
    
    Paper Segment: 
        Image: <image>
        Caption: Figure 1: Distribution of the human ratings in the train/validation and test datasets for different skew factors.
        Fig_id: sp_0031-Figure1-1

    Output:
    {{
        "result": {{'sp_0031-Figure1-1': 0.75}},
        "explanation": "In talk it mentions distribution shift. Talks about data split and skew factor and the test and train data. There this is a fine-grain match."
    }}

    Provide a score for all input paper segment(figure); do not skip any.
    """

    return prompt

def prompt_par_exp(transcript, cand_algo_text, algo_id):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Transcript - {transcript}

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
        The last thing they say, they make the connections to RNNs.
        Now this is a bit detached from the linear transformer, but because they formulated how they do, they can make this connection.
        So this now is valid for all transformers, what they say right here.
        But keep in mind, it is valid for the original transformers in practice if you can make this mapping phi to map to infinite dimensions, which you can't.
        But the analysis is equivalent.
        So they say, look, if we write the attention mechanism like this and therefore like this,
        What we can do is we can define these two quantities, right?
        S and Z. This is what we said before.
        We can actually pre-compute these quantities right here.
        Okay, so that reduces to this right here.
        If now we are looking at a autoregressive transformer, and we said before what an autoregressive transformer was.
        An autoregressive transformer is you have a piece of sequence and you are tasked to predict this next thing right here.
        Now, usually, if you want to train this using an RNN, you have to run your RNN, input this hidden state, then input that, map forward the hidden state.
        So you have to do all of this forward propagation in order to derive at this hidden, at this output right here, make the output, and then you need to back prop through time right here.
        There is no way to what you would like to do is you would like to say here I have a sentence.
        I can actually make like five different training examples from that sentence.
        So the first one is the one you just saw.
        I just block off the last word.
        But I can also make that training example right here, right?
        To when I just cut a second to last word and so on, I can actually make all of these different training examples for language modeling from a single sentence.
        And what I would like to do is I would like to train them all in parallel, right?
        I load my data point once.
        I already have it.
        Why can't I just train everything at the same time?
        Like predict this from this word.
        Now predict also this from these two words.
        And the transformers are, you know, very well conditioned.
        They are very good at this, basically.
        So what a transformer can do is if you input a sequence like, sorry, like the thing at the bottom, you can calculate the training signal for all of these different things at the same time.
        And okay, this was maybe a mistake.
        You can calculate the training signal for all of this at the same time by using what's called causal masking in attention.
        So if I have my attention mechanism right here, let's consider it again.
        Let's consider these two layers.
        If I have my attention mechanism, what I want to do is I want to constrain each token to only attend to tokens that came before it in the sequence.
        So, for example, this token right here, I'm going to constrain it to only attend to itself and the past, because it
        it will predict the next token in the sequence and it would be really easy if we could attend to the input of that token, right?
        It could simply remember what that token is and then aggregate that here and then predict that.
        So if for each token we restrict the attention to the tokens that came before it, like also for this right here, we restrict the attention only to go backwards, then we can train all of this in parallel.
        This is called causal masking.
        It's usually implemented with like a mask that is like an upper diagonal.
        and it's a bit unclear if you can attend to yourself because then I guess this will become the output and you can only attend to this.
        I don't know exactly how it is implemented but it is usually realized with an upper triangular matrix as a mask and you apply this mask to each layer.
        Now they say that
        This is actually like an oranen, and with their formulation you can make this pretty explicit.
        Namely, you have these two states, S and Z, and in each sequence element it's actually like an oranen where you update the S and Z with these quantities right here.
        It's like an RNN where these are the hidden states that you pass forward.
        Then you can formulate any transformer as an RNN that simply updates these two states, but you see you need the explicit mapping of this kernel function.
        You need this explicit mapping in order to be able to do this because otherwise this is here.
        This is not going to be a linear addition.
        It is going to be a complicated and you can't do it by simply remembering the past state.
        So you need that formulation in order to be able to express it as an RNN.
        But their analysis shows that this A-transformer autoregressive is essentially an RNN.
        And you can make a connection in that.
        And you can actually formulate this as an RNN.
        which means that you can train in the transformer fashion, everything at the same time.
        But what is cool about an RNN?
        An RNN at inference time.
        An RNN, once it has produced, you know, this word, it can then, because if you produce auto-regressively, you simply
        say, hey, I have this beginning of my news article, please finish it.
        So the model must output the next word.
        And then from that sequence, it must output the next part, the next word.
        And then from that, the next word and so on.
        And RNN, because of the nature of simply passing forward hidden states,
        at inference time can simply, you know, remember what the hidden states were, input those again, input the output here, and go on.
        So it's pretty fast at inference time, which a transformer isn't.
        With their formulation now, if they have the explicit function phi, they can use this at inference time to be so much faster.
        In fact, on their website, which I'll link of course in the description,
        You can play with image generation using one of these transformers in your browser.
        So you can simply start a transformer run in your browser.
        That's how easy this becomes.
        So you can see the linear transformer with causal masking.
        You'll simply update these states right here and then pass those forward.
        so easy.
        And the backward pass, as we said, I don't want to go into the gradient calculation, but they derive the gradient such that you don't have to remember these hidden states and it becomes or it is linear in or it saves a lot of more memory than before.
        Okay.
    Paper Segment: 
        function forward (φ (Q), φ (K), V ) :\nV'←0,S←0\nfor i = 1, . . . , N do\nS ← S + φ(Ki) V T\nequation 1\nVi ← φ(Qi) S\nend\nreturn V\nend\nunction backward (φ(Q), φ(K), V, G) :\n/* G is the gradient of the loss\nwith respect to the output of\nforward\nS ← 0, φ(Q)L ← 0\nfor i = 1, . . . , N do\nS ← S + φ(Ki) V T\nφ(Qi)L ← GiST\nequation\nend\nS ← 0, φ(K)L ← 0, V L ← 0\nfor i = N, . . . , 1 do\nS ← S + φ (Qi) GT\nVi L ← ST φ(Ki)\nequation 1\nφ(Ki)L ← SVi\nequation 1\nend\nreturn  φ(Q)L, φ(K)L, V L"
        Algo_id: sp_0073_page_5_1

    Output: 
    {{
        "result": {{'sp_0073_page_5_1':0.6}},
        "explanation": "The formulations required are discussed in the talk. Not strongly related not still related"
    }}

    Provide a score for all input paper segment(algorithm); do not skip any.
    """
    return prompt

def prompt_par_eq(transcript, eq_group):
    prompt = f"""
    Your task is to identify how relevant each paper segment is to a given video segment. 
    Inputs:
    Query: Transcript - {transcript}
    Paper Segment: Equations: {eq_group}

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
        Video Segment:
        through it.
        So the forward path of data now looks as follows.
        You come, you start, you say, okay, my data comes in, I will take my weights, that my layer weights, and I will first center them, then scale them with its standard deviation, and then I will use that thing and x in order to obtain my layer output.
        and then I'll send that to the next layer.
        Now the backprop signal here is interesting because the backprop signal comes in from here and splits up in two ways.
        It splits up into the backprop signal.
        Basically you have to backprop through the X times W hat operation.
        We know how to do that.
        That's just a convolutional backprop that you backprop through the convolution operation back to the last layer.
        Now, usually when you backprop through the convolution operation, you get two things.
        You get the derivative with respect to x and you'd get the derivative with respect to the weights w. And you can send both on and you would update your weights with that gradient.
        But now,
        what you'll have to do because this is not your actual parameter of the network, you have to take that particular signal and you have to basically reverse the standardization and the centering before you can apply the gradient.
        But that's all doable.
        The actually modern frameworks will do it by themselves.
        But it's just that the backprop path here, it introduces two new operations to the forward and to the backprop path that you didn't have before.
        But I can imagine this will actually not take, you won't even notice that this is happening.
        This is so fast.
        So the idea is basically pretty basic, especially since the entire discussion around normalization has already happened.
        I enjoy that this paper does go into the theory a bit more, so they analyze what this weight standardization, what effect it has on the Lipschitz constant of the loss, for example.
        And they also research what contributes more, the centering of the weights or the standardization.
        So they kind of run all these ablations where they figure out, okay, if we just do group norm, we have this trajectory here.
        And if we run group norm plus equation five, which is subtracting the mean, you can see the blue and the orange, that is quite a bit.
        And if we only do the dividing by the standard deviation, you can see it's pretty close together.
        But there is a difference.
        If you do both, then again there is a difference to only doing the centering.
        So they say, even though, you know, probably subtracting the mean gives you most of the benefit, since it is so easy, you should just do both.
        And I honestly think and here in the validation error that makes basically no difference at all.
        And they do quite a number of these ablations which I'm not going to go into too much and they do
        Also, so the Lipschitz constant of the loss and the Lipschitz constant of the gradients, they basically show that the loss and the gradients are behaved more, more well behaved when you use this weight standardization technique together with group norm.
        They also do quite a bit of experiments where they show that their method outperforms batch norm and especially in the small batch size regime.
        And that is something that I absolutely believe what happened here.
        Okay.
        I, we actually don't even need to go down there because, um, if you want to read the paper, I invite you to read the paper.
        It's a very good paper.
        I enjoyed reading it.
        Uh, but ultimately they suggest this new method.
        And also I have seen this one replicated across the community a number of times.
        So it seems to be a thing that I would expect either it fizzes out and the community decides that it's about the same as batch norm and therefore not worth it.
        Or, and that's what I believe, since we also go into the direction of larger models, which means smaller batches per worker.
        And generally, batch norm is a pain.
        I believe this is just going to be rather standard in the future.
        So I'll actually incorporate this if I can into my next projects.
        So that was it for me.
        If you like this, consider subscribing, consider leaving a like on the video.
        Thank you for listening.
        If you have any comments, I will very probably read them.
        Bye bye.

        Paper Segment:
        {{
            "sp_0003_page_0003-4": "\\begin{{array}} {{ l }} {{ \\displaystyle \\hat {{ W }} = \\left[ \\hat {{ W }} _ {{ i , j }} \\mid \\hat {{ W }} _ {{ i , j }} = \\frac {{ W _ {{ i , j }} - \\mu _ {{ W _ {{ i , \\cdot }} }} }} {{ \\sigma _ {{ W _ {{ i , \\cdot }} }} }} \\right] , }} \\\\ {{ \\displaystyle y = \\hat {{ W }} * x , }} \\end{{array}}",
            "sp_0001_page_0003-3": "\\forall i \\in [ 1 , \\ldots , N ] : \\mathbf {{ a }} _ {{ i }} = \\mathbf {{W }} _ {{i}} \\mathbf {{h}} _ {{i - 1}} , \\mathbf {{h}} _ {{i}} = f _ {{i}} ( \\mathbf {{a}} _ {{i}} ) ."
        }}
        Output:
        {{
            'result': {{"sp_0003_page_0003-4": 0.75, "sp_0001_page_0003-3":0.3}},
            "explanation": "This sp_0003_page_0003-4 represents weight centering and standardization, where each weight is normalized by subtracting its mean and dividing by its standard deviation, ensuring stabilized and standardized weight distribution. In the explanation they talk about. sp_0001_page_0003-3 is not relevant to what is being told. Not a direct match."
        }}


    Example 2:
        Input:
        Video Segment:
        Hi there.
        Today we're looking at weight standardization by Si Wan Jiao, Hu Yu Wang, Xian Qi Yu, Wei Shen, Alan Yuel of John Hopkins University.
        So weight standardization is a normalization technique for training neural networks.
        And it goes basically in conjunction with another technique called group normalization.
        So if you haven't grouped
        Normalization.
        Norm.
        That is ugly.
        If you haven't seen my video on group normalization and don't know what it is, I suggest you go watch that first or read the group norm paper or some blog post, because weight standardization is usually used together with group norm in order to work well.
        And that's what this paper also says.
        even though it's pretty much independent, but here you can see their main results.
        So if they compare batch norm, group norm and weight standardization used with group norm,
        Then, as you can see here, they can outperform in the ImageNet top one accuracy the other two models.
        And the important part here, as you can see, is batch norm is trained with large batch sizes, while group norm and group norm plus weight standardization are trained with one image per GPU.
        So they have a multi-GPU setup, and this is just one image per GPU.
        And these results over here are on a mask RCNN, which I believe is a recurrent model where the model is large because the model is large and therefore you can only have very small batches per worker.
        And that means batch norm will work less.
        And again, we've discussed why batch norm is not a good thing when you have to go to small batch sizes, because basically what people have discovered is that it is very beneficial in machine learning to normalize your data before working with it.
        What do we mean by it?
        So if you have a bunch of data points right here, and let's say like this,
        It is usually beneficial to first center the data like this.
        So basically calculate its mean and shift it.
        And then to standardize the axis.
        So basically you divide it by the standard deviation in each direction and your data will look something like this.
        Of many classical methods that will improve the conditioning numbers of the requirements to solve it and so on.
        and even of deep learning methods we just know that if you standardize your data like this it works better.
        So people are basically have come up with these methods that where they say well if it helps for the data at the beginning of a neural network then if after a layer
        the data is kind of out of whack that can happen after a layer of neural network.
        We should maybe first, before we send it to the next layer, do the same thing, center it again, and then send it through.
        And if after the next layer again it's out of whack, we should maybe center it and standardize it again before sending it through the next layer.
        So, in each layer you have these transformations that center and standardize the data.
        And usually, for the longest time, this was a batch norm.
        Batch norm does this across the mini batches of the data, since you can't pass the entire data set.
        Now, group norm has come and replaced batch norm because in batch norm, it's very dependent on the batch size, while group norm isn't.
        Now, the group norm paper has sort of made it clear that in competitive batch sizes, in the large batch size regime, group norm is, sorry, batch norm is still the king.
        Batch norm still works better.
        It's only when you go to very small batch sizes that group norm takes over.
        And that's what you can see here.
        So here, okay, it's a bit unfair because batch norm is trained with a larger batch size.
        But even if group norm were to be trained with the large batch size, it would still be in the same place because
        No, it wouldn't.
        It would not.
        Um, sorry.
        That is, that is not the case because the batch is still influence the, uh, gradient stock has to city and so on.
        But still batch norm is better than group norm as you can see here, but here over here, where you kind of have to go to the small batch sizes, uh, then batch norm is all of a sudden worse than group norm.
        And the weight standardization is a technique to actually make group norm better than batch norm in any of these.
        So even in the large batch regime.
        Okay, so we'll now explore weight standardization.
        So in the group norm paper, we've looked at the diagram on the left.
        So basically in batch norm, here is the number of data points.
        This is your batch.
        This is the channels of the individual images, channels.
        And this is the height and width of the image.
        So this is the image itself, a single channel.
        So a single channel in the image would be a column in this thing right here.
        BatchNorm normalizes across the data points in a single channel.
        LayerNorm, which is a precursor to GroupNorm, normalizes only in a single data point instance, but across all of the channels, as you can see here.
        Now that frees its dependence on the batch size.
        Each data point is treated individually.
        But of course, it sort of convolves all the channels with each other.
        It doesn't distinguish

        Paper Segment:
        {{
            "sp_0003_page_0003-4": "\\begin{{array}} {{ l }} {{ \\displaystyle \\hat {{ W }} = \\left[ \\hat {{ W }} _ {{ i , j }} \\mid \\hat {{ W }} _ {{ i , j }} = \\frac {{ W _ {{ i , j }} - \\mu _ {{ W _ {{ i , \\cdot }} }} }} {{ \\sigma _ {{ W _ {{ i , \\cdot }} }} }} \\right] , }} \\\\ {{ \\displaystyle y = \\hat {{ W }} * x , }} \\end{{array}}",
            "sp_0001_page_0003-3": "\\forall i \\in [ 1 , \\ldots , N ] : \\mathbf {{ a }} _ {{ i }} = \\mathbf {{W }} _ {{i}} \\mathbf {{h}} _ {{i - 1}} , \\mathbf {{h}} _ {{i}} = f _ {{i}} ( \\mathbf {{a}} _ {{i}} ) ."
        }}
        {{
            {{
                    "box": [
                    714.7396850585938,
                    986.6026611328125,
                    1034.356689453125,
                    1077.9688720703125
                    ],
                    "text": [
                            "\\begin{{array}} {{ l }} {{ \\displaystyle \\hat {{ W }} = \\left[ \\hat {{ W }} _ {{ i , j }} \\mid \\hat {{ W }} _ {{ i , j }} = \\frac {{ W _ {{ i , j }} - \\mu _ {{ W _ {{ i , \\cdot }} }} }} {{ \\sigma _ {{ W _ {{ i , \\cdot }} }} }} \\right] , }} \\\\ {{ \\displaystyle y = \\hat {{ W }} * x , }} \\end{{array}}"
                        ]
                    "id": "sp_0003_page_0003-4",
                    "page": "sp_0003_page_0003",
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
                "\\forall i \\in [ 1 , \\ldots , N ] : \\mathbf {{ a }} _ {{ i }} = \\mathbf {{ W }} _ {{ i }} \\mathbf {{ h }} _ {{ i - 1 }} , \\mathbf {{ h }} _ {{ i }} = f _ {{ i }} ( \\mathbf {{ a }} _ {{ i }} ) ."
                ],
                "id": "sp_0001_page_0003-3",
                "page": "sp_0001_page_0003",
                "seg_type": "eq"
            }}
        }}

        Output:
        {{
            "result": {{"sp_0003_page_0003-4": 0.3, "sp_0003_page_0003-4": 0.32}},
            "explanation": "This is a intro talk not mentioning or explaining the equation in any way. Both the equations are not mentioned."
        }}



    Provide a score for all input paper segment() do not skip any.
    """

    return prompt