import re
from math import floor

# GOAL: Convert a CFI to a number for Readwise 'location' property. This number is a 'position' throughout the book
# The lower the number, the closer to the start of the book it is

highlights = [
    {
      "end_cfi": "/2/4/2/66/2/1:31",
      "highlighted_text": "Cover Design by Oliver Ferreira",
      "spine_index": 2,
      "spine_name": "text/part0000_split_001.html",
      "start_cfi": "/2/4/2/66/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-20T11:11:11.294Z",
      "type": "highlight",
      "uuid": "TDzdkrbT8QLGJbOIf7PcuA"
    },
    {
      "end_cfi": "/2/4/4/4/2/1:16",
      "highlighted_text": "Everybody writes",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/4/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-20T11:11:49.002Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "ECFjC40ZvzxRm4W7jAi7XQ"
    },
    {
      "end_cfi": "/2/4/4/4/2/1:772",
      "highlighted_text": "Every intellectual endeavour starts with a note.",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/4/2/1:724",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T11:25:53.110Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "PfuFj7HgMlWdDtRRzEIwrA"
    },
    {
      "end_cfi": "/2/4/4/8/2/1:571",
      "highlighted_text": "improving the organisation of all writing makes a difference.",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/8/2/1:522",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T11:30:44.807Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "56yNKWGh3_FDdccrU5aO_w"
    },
    {
      "end_cfi": "/2/4/4/8/2/1:758",
      "highlighted_text": "the actual writing down of the argument is the smallest part of its development.",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/8/2/1:678",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T11:30:51.898Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "Dykyq66iC6oJCRmBq84CnA"
    },
    {
      "end_cfi": "/2/4/4/8/2/1:962",
      "highlighted_text": "build up a treasure of smart and interconnected notes along the way",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/8/2/1:895",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T11:31:00.550Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "kTwqZoa_2tLrWp46xqt38A"
    },
    {
      "end_cfi": "/2/4/4/8/2/1:1197",
      "highlighted_text": "you can write every day in a way that brings your projects forward.",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/8/2/1:1130",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T11:41:38.633Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "kYI12cq68RLxsUj1RHO46g"
    },
    {
      "end_cfi": "/2/4/4/10/2/1:719",
      "highlighted_text": "those who take smart notes will never have the problem of a blank screen again.",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/10/2/1:640",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T11:44:45.207Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "asYI1uwePUoyRMZH5JBGCg"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:980",
      "highlighted_text": "good, productive writing is based on good note-taking",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/14/2/1:927",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:08:45.358Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "gIKZO29zcy6oN9exYFrR4w"
    },
    {
      "end_cfi": "/2/4/4/20/2/1:147",
      "highlighted_text": "It is not so important who you are, but what you do. Doing the work required and doing it in a smart way leads, somehow unsurprisingly, to success.",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/20/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:09:39.513Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "NzXcqUO-Ne0gujtoZI1-3w"
    },
    {
      "end_cfi": "/2/4/4/22/2/1:202",
      "highlighted_text": "self-control and self-discipline have much more to do with our environment than with ourselves (cf. Thaler, 2015, ch. 2) – and the environment can be changed",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/22/2/1:57",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:10:43.550Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "9CnzZHJcf9AXaGJ6UQUj7w"
    },
    {
      "end_cfi": "/2/4/4/22/2/1:281",
      "highlighted_text": "Nobody needs willpower not to eat a chocolate bar when there isn’t one around",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/22/2/1:204",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:10:53.409Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "Fg2snuATiblo9OKxlXyPcg"
    },
    {
      "end_cfi": "/2/4/4/22/2/1:424",
      "highlighted_text": "nobody needs willpower to do something they wanted to do anyway. Every task that is interesting, meaningful and well-defined will be done",
      "spine_index": 5,
      "spine_name": "text/part0000_split_004.html",
      "start_cfi": "/2/4/4/22/2/1:287",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:11:23.972Z",
      "toc_family_titles": [
        "Introduction"
      ],
      "type": "highlight",
      "uuid": "L2rbnIv6hg5KwVt8riHbNA"
    },
    {
      "end_cfi": "/2/4/4/6/2/1:260",
      "highlighted_text": "If you can trust the system, you can let go of the attempt to hold everything together in your head and you can start focusing on what is important",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/6/2/1:125",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:12:55.054Z",
      "toc_family_titles": [
        "1 Everything You Need to Know"
      ],
      "type": "highlight",
      "uuid": "h-cp6tC1kakMtyK7uZspJQ"
    },
    {
      "end_cfi": "/2/4/4/10/2/1:857",
      "highlighted_text": "It is a huge misunderstanding that the only alternative to planning is aimless messing around",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/10/2/1:764",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:45:24.073Z",
      "toc_family_titles": [
        "1 Everything You Need to Know"
      ],
      "type": "highlight",
      "uuid": "3O-Kje4x7FeFxvn6YosLfA"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:166",
      "highlighted_text": "it is usually the best students who struggle the most.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/14/2/1:112",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:46:31.880Z",
      "toc_family_titles": [
        "1 Everything You Need to Know"
      ],
      "type": "highlight",
      "uuid": "lx81YrKCXOZlVrit0Uc2Ew"
    },
    {
      "end_cfi": "/2/4/4/20/2[BC-245f05fb8f7d49b2b04f785a906cc2f5]/1:668",
      "highlighted_text": "writing is not only for proclaiming opinions, but the main tool to achieve insight worth sharing",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/20/2[BC-245f05fb8f7d49b2b04f785a906cc2f5]/1:572",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:48:14.714Z",
      "toc_family_titles": [
        "1.1 Good Solutions are Simple – and Unexpected"
      ],
      "type": "highlight",
      "uuid": "rqHTxRCVmVBwe8tCNe6Nhw"
    },
    {
      "end_cfi": "/2/4/4/34/2/1:516",
      "highlighted_text": "The new way of working might feel artificial at first and not necessarily like what you intuitively would do. That is normal.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/34/2/1:391",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:55:14.555Z",
      "toc_family_titles": [
        "1.1 Good Solutions are Simple – and Unexpected"
      ],
      "type": "highlight",
      "uuid": "icDLqsZbxUaCOIcS5M9V4g"
    },
    {
      "end_cfi": "/2/4/4/36/2/1:691",
      "highlighted_text": "Only if we know that everything is taken care of, from the important to the trivial, can we let go and focus on what is right in front of us.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/36/2/1:550",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T12:55:59.415Z",
      "toc_family_titles": [
        "1.1 Good Solutions are Simple – and Unexpected"
      ],
      "type": "highlight",
      "uuid": "XjNzyQ6T1xKzqMHTBsjFxQ"
    },
    {
      "end_cfi": "/2/4/4/44/2/1:513",
      "highlighted_text": "Only if you can trust your system, only if you really know that everything will be taken care of, will your brain let go and let you focus on the task at hand.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/44/2/1:354",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:28:56.846Z",
      "toc_family_titles": [
        "1.1 Good Solutions are Simple – and Unexpected"
      ],
      "type": "highlight",
      "uuid": "uyoIPQAOJv-SKuwuQcDwJg"
    },
    {
      "end_cfi": "/2/4/4/56/2/1:358",
      "highlighted_text": "Just amassing notes in one place would not lead to anything other than a mass of notes",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/56/2/1:272",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:33:11.533Z",
      "toc_family_titles": [
        "1.2 The Slip-box"
      ],
      "type": "highlight",
      "uuid": "oLL_VnBWvabHK_WreJ3PGA"
    },
    {
      "end_cfi": "/2/4/4/76/2/1:446",
      "highlighted_text": "doesn’t it make much more sense that the impressive body of work was produced not in spite of the fact he never made himself do anything he didn’t feel like, but because of it?",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/76/2/1:277",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:37:46.201Z",
      "toc_family_titles": [
        "1.2 The Slip-box"
      ],
      "type": "highlight",
      "uuid": "r5e5d3ZUczr6orex1b2dnw"
    },
    {
      "end_cfi": "/2/4/4/80/2/1:327",
      "highlighted_text": "If we work in an environment that is flexible enough to accommodate our work rhythm, we don’t need to struggle with resistance.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/80/2/1:200",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:39:17.321Z",
      "toc_family_titles": [
        "1.2 The Slip-box"
      ],
      "type": "highlight",
      "uuid": "IzFK3xY4krX2AYCXsVfyew"
    },
    {
      "end_cfi": "/2/4/4/80/2/1:636",
      "highlighted_text": "Studies on highly successful people have proven again and again that success is not the result of strong willpower and the ability to overcome resistance, but rather the result of smart working environments that avoid resistance in the first place (cf. Neal et al. 2012; Painter et al. 2002; Hearn et al. 1998).",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/80/2/1:328",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:39:22.207Z",
      "toc_family_titles": [
        "1.2 The Slip-box"
      ],
      "type": "highlight",
      "uuid": "Y3FGgFCVwyzX7wER5OQinQ"
    },
    {
      "end_cfi": "/2/4/4/82/2/1:472",
      "highlighted_text": "if you don’t have an external system to think in and organise your thoughts, ideas and collected facts, or have no idea how to embed it in your overarching daily routines, the disadvantage is so enormous that it just can’t be compensated by a high IQ",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/82/2/1:242",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:43:10.105Z",
      "toc_family_titles": [
        "1.2 The Slip-box"
      ],
      "type": "highlight",
      "uuid": "N5hfJfJV9wvi_qu8GDVG1w"
    },
    {
      "end_cfi": "/2/4/4/90/6/1:236",
      "highlighted_text": "Intuitively, most people do not expect much from simple ideas. They rather assume that impressive results must have equally impressively complicated means",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/90/6/1:82",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:44:09.243Z",
      "toc_family_titles": [
        "1.2 The Slip-box"
      ],
      "type": "highlight",
      "uuid": "NyC3iOhvZo1UQt5tnVGhuA"
    },
    {
      "end_cfi": "/2/4/4/100/2/1:250",
      "highlighted_text": "Strictly speaking, Luhmann had two slip-boxes: a bibliographical one, which contained the references and brief notes on the content of the literature, and the main one in which he collected and generated his ideas, mainly in response to what he read.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/100/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:44:55.395Z",
      "toc_family_titles": [
        "1.3 The slip-box manual"
      ],
      "type": "highlight",
      "uuid": "wRgaTadnmHORURRNmAalVQ"
    },
    {
      "end_cfi": "/2/4/4/104/2/1:316",
      "highlighted_text": "Whenever he read something, he would write the bibliographic information on one side of a card and make brief notes about the content on the other side (Schmidt 2013, 170). These notes would end up in the bibliographic slip-box.\n\nIn a second step, shortly after, he would look at his brief notes and think about their relevance for his own thinking and writing. He then would turn to the main slip-box and write his ideas, comments and thoughts on new pieces of paper, using only one for each idea and restricting himself to one side of the paper",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/102/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "blue"
      },
      "timestamp": "2023-08-18T13:47:38.575Z",
      "toc_family_titles": [
        "1.3 The slip-box manual"
      ],
      "type": "highlight",
      "uuid": "bnsVozUcAkEFTSgaiE1XLw"
    },
    {
      "end_cfi": "/2/4/4/108/2/1:244",
      "highlighted_text": "He did not just copy ideas or quotes from the texts he read, but made a transition from one context to another. It was very much like a translation where you use different words that fit a different context, but strive to keep the original meaning",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/108/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:52:41.465Z",
      "toc_family_titles": [
        "1.3 The slip-box manual"
      ],
      "type": "highlight",
      "uuid": "7tEx7tWMIvwNjfQQttZ9Lg"
    },
    {
      "end_cfi": "/2/4/4/112/2/1:116",
      "highlighted_text": "Whenever he added a note, he checked his slip-box for other relevant notes to make possible connections between them",
      "notes": "Actively looks to link it. No orphans",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/112/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:53:53.527Z",
      "toc_family_titles": [
        "1.3 The slip-box manual"
      ],
      "type": "highlight",
      "uuid": "Yu-NzvVOlZuB3cw7G5JIfQ"
    },
    {
      "end_cfi": "/2/4/4/114/2/1:318",
      "highlighted_text": "While other systems start with a preconceived order of topics, Luhmann developed topics bottom up, then added another note to his slip-box, on which he would sort a topic by sorting the links of the relevant other notes.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/114/2/1:98",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:54:17.381Z",
      "toc_family_titles": [
        "1.3 The slip-box manual"
      ],
      "type": "highlight",
      "uuid": "DNAlf81FkOZbzZjCTsgskg"
    },
    {
      "end_cfi": "/2/4/4/120/2/1:399",
      "highlighted_text": "We need a reliable and simple external structure to think in that compensates for the limitations of our brains.",
      "spine_index": 6,
      "spine_name": "text/part0000_split_005.html",
      "start_cfi": "/2/4/4/120/2/1:287",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:54:41.496Z",
      "toc_family_titles": [
        "1.3 The slip-box manual"
      ],
      "type": "highlight",
      "uuid": "yEqarPBawVva09GBKku7cA"
    },
    {
      "end_cfi": "/2/4/4/8/2/1:525",
      "highlighted_text": "Only with a less narrow focus will you be able to see connections and patterns",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/8/2/1:447",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:56:50.774Z",
      "toc_family_titles": [
        "2 Everything You Need to Do"
      ],
      "type": "highlight",
      "uuid": "riwhmCvVQw6DzCh3oQn1sg"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:335",
      "highlighted_text": "Writing these notes is also not the main work. Thinking is. Reading is. Understanding and coming up with ideas is",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/14/2/1:222",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:57:26.908Z",
      "toc_family_titles": [
        "2 Everything You Need to Do"
      ],
      "type": "highlight",
      "uuid": "HzUE8wNThc6mOCOBOFmIQw"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:742",
      "highlighted_text": "Writing notes accompanies the main work and, done right, it helps with it. Writing is, without dispute, the best facilitator for thinking, reading, learning, understanding and generating ideas we have",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/14/2/1:553",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T13:57:41.678Z",
      "toc_family_titles": [
        "2 Everything You Need to Do"
      ],
      "type": "highlight",
      "uuid": "ktGIJKo184cTFO20o3NCXg"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:1540",
      "highlighted_text": "Levy writes: “no m",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/14/2/1:1522",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-20T10:42:50.243Z",
      "toc_family_titles": [
        "2 Everything You Need to Do"
      ],
      "type": "highlight",
      "uuid": "6_xQ4NHzAO-88X_2a_-vpg"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:1806",
      "highlighted_text": "If there is one thing the experts agree on, then it is this: You have to externalise your ideas, you have to write.",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/14/2/1:1691",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T15:44:20.353Z",
      "toc_family_titles": [
        "2 Everything You Need to Do"
      ],
      "type": "highlight",
      "uuid": "2h-P86PdhDtVyIquUu6Xkw"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:2096",
      "highlighted_text": "if we have to write anyway, why not use our writing to build up the resources for our future publications?",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/14/2/1:1990",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T15:44:39.251Z",
      "toc_family_titles": [
        "2 Everything You Need to Do"
      ],
      "type": "highlight",
      "uuid": "RB4ITi5GOFhIp84mzfidPA"
    },
    {
      "end_cfi": "/2/4/4/18/6/2/1:28",
      "highlighted_text": "Writing a paper step by step",
      "notes": "1. Make fleeting notes.\n2. Make literature notes\n3. Make permanent notes",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/18/6/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-18T19:31:29.370Z",
      "toc_family_titles": [
        "2.1 Writing a paper step by step"
      ],
      "type": "highlight",
      "uuid": "G4x5x-qS0wzKSwmEX_87xA"
    },
    {
      "end_cfi": "/2/4/4/24/4/1:639",
      "highlighted_text": "The idea is not to collect, but to develop ideas, arguments and discussions. Does the new information contradict, correct, support or add to what you already have (in the slip-box or on your mind)? Can you combine ideas to generate something new? What questions are triggered by them?   ",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/24/4/1:352",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-19T17:05:44.866Z",
      "toc_family_titles": [
        "2.1 Writing a paper step by step"
      ],
      "type": "highlight",
      "uuid": "EF8ROrRDdenhJM90klNULQ"
    },
    {
      "end_cfi": "/2/4/4/24/4/1:1033",
      "highlighted_text": "Throw away the fleeting notes from step one and put the literature notes from step two into your reference system. You can forget about them now. All that matters is going into the slip-box.",
      "spine_index": 7,
      "spine_name": "text/part0000_split_006.html",
      "start_cfi": "/2/4/4/24/4/1:843",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-19T17:06:33.508Z",
      "toc_family_titles": [
        "2.1 Writing a paper step by step"
      ],
      "type": "highlight",
      "uuid": "LPClH2GrxURt7zdLSiNFNw"
    },
    {
      "end_cfi": "/2/4/4/14/2/1:202",
      "highlighted_text": "The trick is not to try to break with old habits and also not to use willpower to force oneself to do something else, but to strategically build up new habits that have a chance to replace the old ones.",
      "spine_index": 21,
      "spine_name": "text/part0000_split_020.html",
      "start_cfi": "/2/4/4/14/2/1:0",
      "style": {
        "kind": "color",
        "type": "builtin",
        "which": "yellow"
      },
      "timestamp": "2023-08-20T12:48:20.783Z",
      "toc_family_titles": [
        "14 Make It a Habit"
      ],
      "type": "highlight",
      "uuid": "lrsGvcaG5geDkxzJlDZlqQ"
    }
  ]

# highlights = [
# {
#       "highlighted_text": "Writing a paper step by step",
#       "spine_index": 7,
#       "start_cfi": "/2/4/4/18/6/2/1:0",
#       "uuid": "G4x5x-qS0wzKSwmEX_87xA"
#     },
#     {
#       "highlighted_text": "The idea is not to collect, but to develop ideas, arguments and discussions. Does the new information contradict, correct, support or add to what you already have (in the slip-box or on your mind)? Can you combine ideas to generate something new? What questions are triggered by them?   ",
#       "spine_index": 7,
#       "start_cfi": "/2/4/4/24/4/1:0",
#       "uuid": "EF8ROrRDdenhJM90klNULQ"
#     }
# ]

# First x steps are boosted, rest are added/multiplied by 1
# This is messy and crap, but seems to work - what's the easy way of doing this?
# TODO: look at this across more books. Maybe this falls down massively with smaller or larger books? Or an annotation right at the end of an early section vs an annotation right at the start of a later section?
def calculatePosition(spine_index, cfi):
    stepsToBoost = 6
    boostMultiplier = 500
    boostTotal = (boostMultiplier * stepsToBoost)

    steps = re.findall("(?<=\/)\d+", cfi)
    charPos = int(re.search(":(\d+)", cfi).group(1)) # character position on page
    stepsTotal = sum([int(cfiStep) * ((i + 1) * max([(boostTotal - (i * boostMultiplier)), 1])) for i, cfiStep in enumerate(steps)])

    return floor(
        (
          (spine_index * (boostMultiplier * 5000)) +
          stepsTotal +
          ((charPos+1) * 10)
        ) / 10000
    )

for highlight in highlights:
    print(highlight['uuid'], calculatePosition(highlight['spine_index'], highlight['start_cfi']))
