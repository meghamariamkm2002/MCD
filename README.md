# Unifying Scientific Communication: Fine-Grained Correspondence Across Scientific Media

**Accepted at CVPR Finding 2026**

<p align="left">
  <a href="#-quick-start"><b>Quick Start</b></a> |
  <a href="https://meghamariamkm2002.github.io/mcd_2026/"><b>ProjectPage</b></a> |
  <a href=""><b>arXiv</b></a> |
  <a href=""><b>Citation</b></a> <br>
</p>

## 🎩Abstract

The communication of scientific knowledge has become increasingly multimodal, spanning text, visuals, and speech through materials such as research papers, slides, and recorded presentations. These different representations collectively convey a study’s reasoning, results, and insights, offering complementary perspectives that enrich understanding. However, despite their shared purpose, such materials are rarely connected in a structured way. The absence of explicit links across formats makes it difficult to trace how concepts, visuals, and explanations correspond, limiting unified exploration and analysis of research content. To address this gap, we introduce the \textit{Multimodal Conference Dataset (MCD)}, the first benchmark that integrates research papers, presentation videos, explanatory videos, and slides from the same works. We evaluate a range of embedding-based and vision–language models to assess their ability to discover fine-grained cross-format correspondences, establishing the first systematic benchmark for this task. Our results show that vision–language models are robust but struggle with fine-grained alignment, while embedding-based models capture text–visual correspondences well but equations and symbolic content form distinct clusters in the embedding space. These findings highlight both the strengths and limitations of current approaches and point to key directions for future research in multimodal scientific understanding.

## 🚀 Quick Start

## Directory Structure

### Prompts/
Contains prompts used for vision–language models (VLMs), along with corresponding few-shot examples for each task.

### Dataset/

#### EXP/
Explanatory Set samples.
- `vid_seg/`: Video segments with transcripts (`trans`)
- `pap_seg/`: Paper segments including paragraphs (`par`), figures (`fig`), algorithms (`algo`), and equations (`eq`)

#### PRES/
Presentation Set samples.
- `vid_seg/`: Video segments with transcripts (`trans`) and slides
- `pap_seg/`: Paper segments including paragraphs (`par`), figures (`fig`), algorithms (`algo`), and equations (`eq`)

### Environment

```
git clone https://github.com/meghamariamkm2002/MCD.git
cd MCD
```


# Citation
If you find our benchmark/code useful, feel free to leave a star and please cite our paper as follows:
```
@inproceedings{mcd_2026,
    title={Unifying Scientific Communication: Fine-Grained Correspondence Across Scientific Media},
    author={Megha Mariam K M and Vineeth N. Balasubramanian and C. V. Jawahar},
    booktitle={Findings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    year={2026}
}
```





