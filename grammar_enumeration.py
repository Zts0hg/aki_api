import pandas as pd

grammars = [
    {
        "content": "~ 際 (に)",
        "hiragana": "~ さい(に)",
        "meaning": "~とき 硬い言い方（…………时候。书面语。）",
        "usage": "名の・動 辞書形/た形 + 際(に)",
        "example": [{
            "content": "① この整理券は、 商品受け取りの際、必要です。",
            "hiragana": "このせいりけんは、 しょうひんうけとりのさい、ひつようです。",
            "meaning": "这张排号单在领取商品时需要用到。"
        }, {
            "content": "②こちらの会議室をご利用になる際は、 受付で必要事項をご記入ください。",
            "hiragana": "こちらのかいぎしつをごりようになるさいは、 うけつけでひつようじこうをごきにゅうください。",
            "meaning": "使用这间会议室时,请在前台登记必要事项。"
        }, {
            "content": "③アメリカの大統領は来日した際に、 わたしたちの大学でスピーチを行った。",
            "hiragana": "アメリカのだいとうりょうはらいにちしたさいに、 わたしたちの大学でスピーチを行った。",
            "meaning": "美国总统访问日本时,在我们大学做了演讲。"
        }],
        "remark": "主要接在表达行为、事件等的动词 (「使う・完成する」等) 和名詞 (「搭乗・外出」 等)后。多用于公共场合等,不太用于日常的普通事情。",
        "source": ""
    },
    {
        "content": "~に際して~にあたって",
        "hiragana": "~にさいして~にあたって",
        "meaning": """⇒~するとき 硬い言い方\n当・・・・・・ 的時候。书面語。""",
        "usage": "名・ 辞書形 + に際してにあたって",
        "example": [
            {
                "content": "① 工事関係者は工事を始めるに際して、 近所の住民にあいさつをして回った。",
                "hiragana": "",
                "meaning": "施工人员在开始施工前,走访问候了附近的住户。"
            },
            {
                "content": "② 当ショッピングサイトのご利用に際して、以下のご利用条件をよくお読みください。",
                "hiragana": "",
                "meaning": "使用本购物网站时,请仔细阅读以下使用条款。"
            },
            {
                "content": "③ 新しく事業を始めるにあたって、しっかりと準備をしようと思っております。",
                "hiragana": "",
                "meaning": "在新开展一项业务之际,我想做好充分的准备。"
            },
            {
                "content": "④ お二人の門出にあたりまして、 お祝いの言葉を申し上げます。",
                "hiragana": "",
                "meaning": "值此二位迎接新生活之际,送上我的祝福。"
            },
            {
                "content": "⑤ 日本で国際会議を開催するにあたり、関係各方面からの協力を得た。",
                "hiragana": "",
                "meaning": "在日本召开国际会议之际,得到了相关各方面的支持与配合。"
            },
        ],
        "remark": "前接表达某种场合仅此一次的、人的意志性的行为,且是某个特殊时刻的词语(「結婚「店を開く」等)。后接叙述人的行為的句子。「〜にあたって」 前接表込更加和板的行為的詞語,不能接消板意的語 (「別れ・入院・倒産」等)。",
        "source": "",
    },
    {
        "content": "〜たとたん (に)",
        "hiragana": "",
        "meaning": """⇒~したら、直後に意外なことが起こる。
做了…………之后,紧接着发生意外的事情。""",
        "usage": "動た形 + とたん (に)",
        "example": [
            {
                "content": "① 山の頂上でワインを一口飲んだとたんに、 めまいがした。",
                "hiragana": "",
                "meaning": "在山顶上刚喝了一口葡萄酒就头晕了。"
            },
            {
                "content": "② 夫は結婚前は優しかったが、結婚したとたんに、 態度が変わった。",
                "hiragana": "",
                "meaning": "百丈夫在婚前很温柔,但是一结婚,态度就变了。"
            },
            {
                "content": "③ 国の母に電話をかけた。 母の声を聞いたとたん、 涙があふれてきた。",
                "hiragana": "",
                "meaning": "给家乡的妈妈打了电话。一听到妈妈的声音,我就热泪盈眶。"
            },
            {
                "content": "④ 僕が 「さよなら」 と言ったとたん、 彼女は走っていってしまった。",
                "hiragana": "",
                "meaning": "我刚一说“再见”,她就跑开了。"
            },
        ],
        "remark": """前接表込瞬間結束意又的功作和変化的詞 (「立ち上がる変わる」等)。 后句接意外
性的内容。不接表达说话人希望、意志的句子(~)」等),以及要求听话人做某事
的句子(「~ませんか~なさい」等)。""",
        "source": "",
    },
    {
        "content": "~(か)と思うと・~ (か) と思ったら",
        "hiragana": "~(か)とおもうと・~ (か) とおもったら",
        "meaning": """⇒ 〜の後、すぐに続いて次の出来事や大きな変化が起こる。
……之后,紧接着马上发生下一个事件或重大变化。""",
        "usage": "動た形 + (か)と思うと(か) と思ったら",
        "example": [
            {
                "content": "① 林さんは部屋に入ってきたかと思うと、 いきなり窓を全部開けた。",
                "hiragana": "",
                "meaning": "小林刚一进房间,就突然把窗戶全部打开了"
            },
            {
                "content": "② 赤ちゃんは今泣いたと思うと、もう笑っている。",
                "hiragana": "",
                "meaning": "小宝宝刚才还哭呢,现在又笑了起来。"
            },
            {
                "content": "③ やっと部屋が片付いたかと思ったら、子供たちがすぐまた散らかした。",
                "hiragana": "",
                "meaning": "好不容易收拾好房间,孩子们马上又弄乱了。"
            },
            {
                "content": "④ このごろは気温の差が大きい。 昨日は暑くなったかと思ったら、 今日は涼しい。",
                "hiragana": "",
                "meaning": "最近溫差很大。昨天还很热,今天又很凉爽。"
            },
        ],
        "remark": """不能用于能力上无法做到的事情。主语通常为第一人称。""",
        "source": "",
    },
    {
        "content": "〜か〜ないかのうちに",
        "hiragana": "",
        "meaning": """⇒~が終わると同時に、次のことが起こる。
………结束的同时,发生下一件事情。""",
        "example": [
            {
                "content": "① 一郎はベッドに横になるかならないかのうちに、ぐっすり眠ってしまった。",
                "hiragana": "",
                "meaning": "太郎一躺到床上就酣然入睡了。"
            },
            {
                "content": "② わたしは夜が明けたか明けないかのうちに家を出て、空港へ向かった。",
                "hiragana": "",
                "meaning": "隔天一亮我就出了家门,前往机场。"
            },
            {
                "content": "③ あの作家は今売れっ子だ。 話題作を発表したかしないかのうちに、もう次の作品に取りかかっ",
                "hiragana": "",
                "meaning": "那个作家现在很走红。听说刚一发表热门作品,就马上着手下一部作品。"
            },
        ],
        "usage": "辞書形/た形 + か+ 動 ない形 + かのうちに",
        "remark": """前接表込瞬間結束意叉的幼作和変化的幼詞(「着く・終わる」等)。 后面不接表込税活
人的意志,以及要求听活人做某事的句子。与「~(か)と思うと~(か)と思った
6」相比,“几乎同时发生”的语气更强烈。""",
        "source": "",
    },
    {
        "content": "~最中だ",
        "hiragana": "~さいちゅうだ",
        "meaning": """⇒ちょうど~しているところだ。
正在做......的时候。""",
        "example": [
            {
                "content": "① 田中さんは今考えごとをしている最中だから、じゃましないほうがいい。",
                "hiragana": "",
                "meaning": "田中现在正在思考事情,所以还是不要打扰为好。"
            },
            {
                "content": "② 浜辺でバーベキューをやっている最中に、 急に雨が降り出した。",
                "hiragana": "",
                "meaning": "正在海边烧烤的时候,突然下起雨来。"
            },
            {
                "content": "③ スピーチの最中に、 突然電気が消えた。",
                "hiragana": "",
                "meaning": "留正在演讲的时候,突然停电了。"
            },
        ],
        "usage": "名の動 ている形 + 最中だ",
        "remark": """前接表示在較短時間內迸行的劫作的詞語(「試験・書いている」等)。 「~最中に」的
后面多接“发生了妨碍此事的意想不到的事情”这种含义的句子。""",
        "source": "",
    },
    {
        "content": "〜うちに",
        "hiragana": "",
        "meaning": """A⇒時間の制限があって、 〜でなくなった後では実現が難しいから、その前にしてしまう。
因为有时间限制,如果变得不......之后那就很难实现,所以要赶在这种变化发生之前完成。
B ⇒ ~している間に変化が現れる。
正在做......期间发生了变化。""",
        "example": [
            {
                "content": "① 家事は、 子供が眠っているうちに、 全部やってしまった。",
                "hiragana": "",
                "meaning": "留趁着孩子睡觉,把家务活全部干完了。"
            },
            {
                "content": "② 忘れないうちに、カレンダーにメモしておこう。",
                "hiragana": "",
                "meaning": "趁着没忘,先记在日历上吧。"
            },
            {
                "content": "③ 足が丈夫なうちに、ヒマラヤ登山を計画したい。",
                "hiragana": "",
                "meaning": "趁着腿脚还结实灵便,计划攀登喜马拉雅山。"
            },
            {
                "content": "④ 学生のうちに車の運転免許を取ろうと思っています。",
                "hiragana": "",
                "meaning": "我想趁着上学期间,考取驾照。"
            },
            {
                "content": "⑤ インターネットで調べているうちに、いろいろなことがわかってきた。",
                "hiragana": "",
                "meaning": "上网查阅期间,了解到了很多事情。"
            },
            {
                "content": "⑥ この携帯電話は、長い間使っているうちに、もう自分の体の一部のようになった。",
                "hiragana": "",
                "meaning": "这部手机在长期使用的过程中,已经变成了自己身体的一部分。"
            },
            {
                "content": "⑦ 知らないうちに、雨が降り始めていた。",
                "hiragana": "",
                "meaning": "不知不觉间下起雨来。"
            },
        ],
        "usage": """A 因为有时间限制,如果变得不......之后那就很难实现,所以要赶在这种变化发生之前完成。
(名-の・動 辞書形 / ている / ない形・イ形 い・ ナ形 な + うちに)

B 正在做......期间发生了变化。
(動 辞書形 / ている形/ない形 + うちに)
""",
        "remark": """A 因为有时间限制,如果变得不......之后那就很难实现,所以要赶在这种变化发生之前完成。
(前接有时间跨度的词语。后续表达人的意志性动作的动词句。)

B 正在做......期间发生了变化。
(前接有时间跨度的词语。后续不含人的意志性行为动作,以及表达变化的句子。)""",
        "source": "",
    },
    {
        "content": "〜ばかりだ• ~一方だ",
        "hiragana": "〜ばかりだ• ~いっぽうだ",
        "meaning": """⇒~という一方方向に変化が進んでいく。
变化朝着......单一方向不断加剧。""",
        "example": [
            {
                "content": "① このごろは仕事が多くて残業が増えるばかりだ。",
                "hiragana": "",
                "meaning": "民最近工作很多,一直在不停地加班。"
            },
            {
                "content": "② 東京の交通機関は複雑になるばかりで、 わたしはよくわからなくなってきた。",
                "hiragana": "",
                "meaning": "东京的交通越来越复杂,我越来越搞不懂了。"
            },
            {
                "content": "③ 一度問題が起きてから、 彼との人間関係は悪くなる一方だ。",
                "hiragana": "",
                "meaning": "发生了一次摩擦之后,我和他的关系就变得越来越差。"
            },
            {
                "content": "④ 牛や豚の病気が広がる一方なので、国中の人が心配している。",
                "hiragana": "",
                "meaning": "牛、猪等的疫情不断蔓延,全国人民都很担忧。"
            },
        ],
        "usage": "動 辞書形 + ばかりだ ・ 一方だ",
        "remark": """前接表示変化的効詞 (「増える・悪くなる」 等)。「~ばかりだ」 多表示朝着不好的方
向发展。""",
        "source": "",
    },
    {
        "content": "~(よ) うとしている",
        "hiragana": "",
        "meaning": """⇒ 〜という変化が起こる少し前だ・もうすぐ〜する。硬い言い方
在……这个变化发生的前一刻、马上就要...……。书面语。""",
        "example": [
            {
                "content": "① さあ、 決勝戦が今、始まろうとしています。 みんな緊張しています。",
                "hiragana": "",
                "meaning": "呀,决赛即将开始。大家都很紧张。"
            },
            {
                "content": "② 駅前に30階建ての高級マンションが完成しようとしている。",
                "hiragana": "",
                "meaning": "车站前的三十层高的高级公寓即将竣工。"
            },
            {
                "content": "③ 桜が満開になろうとしているとき、 雪が降った。",
                "hiragana": "",
                "meaning": "櫻花即将完全盛开之时,下雪了。"
            },
        ],
        "usage": "動う・よう形 + としている",
        "remark": """前接表示瞬間完成意乂的幼詞(「始まる・幕が開く」等)。""",
        "source": "",
    },
    {
        "content": "~つつある",
        "hiragana": "",
        "meaning": """⇒~という変化が進行中だ。 硬い言い方
…………变化正在进行过程中。书面语。""",
        "example": [
            {
                "content": "① 次第に暖かくなりつつあります。 春はもうすぐです。",
                "hiragana": "",
                "meaning": "天气渐渐变暖。春天快到了。"
            },
            {
                "content": "② この会社は現在発展しつつあり、 将来が期待される。",
                "hiragana": "",
                "meaning": "这家公司不断发展壮大,未来值得期待。"
            },
            {
                "content": "③ 明治時代の初め、 日本は急速に近代化しつつあった。",
                "hiragana": "",
                "meaning": "明治初期,日本迅速实现了现代化。"
            },
        ],
        "usage": "動ます + つつある",
        "remark": """前接表示変化意又的幼詞(「暖かくなる・広がる」等)。""",
        "source": "",
    },
    {
        "content": "〜つつ",
        "hiragana": "",
        "meaning": """⇒ 〜ながら、 あることをする。硬い言い方
一边……,一边做某事。书面语。""",
        "example": [{
            "content": "① この空き地をどうするかについては、住民と話し合いつつ、計画を立てていきたい。",
            "hiragana": "",
            "meaning": "关于这块空地如何处理的问题,我们打算一边与居民商讨,一边制订计划。"
        }, {
            "content": "② 将来の仕事のこと、 お金のことなどを考えつつ、 進路を選ばなければならない。",
            "hiragana": "",
            "meaning": "必须考虑到将来的工作和收入等,来决定今后的出路。"
        }, {
            "content": "③ いろいろな体験を楽しみつつ、日本の生活に慣れていった。",
            "hiragana": "",
            "meaning": "一边享受着各种各样的体验,一边去适应日本的生活。"
        }],
        "usage": "動ます + つつ",
        "remark": """前接表示有肘同跨度意的行為劫詞(「考える」等)。「~つつ」的前后句是同一主語。""",
        "source": "",
    },
    {
        "content": "~てはじめて",
        "hiragana": "",
        "meaning": """⇒~を経験した後や、 〜という状態になった後で、 今までになかったことが起こる。
经历……以后,或者变成…………状态以后,发生了以前未出现过的事情。""",
        "example": [{
            "content": "① 実際に現地の様子を見てはじめて、今回の地震のひどさを知った。",
            "hiragana": "",
            "meaning": "实际看了现场的情况之后,才知道这次地震的严重性。"
        }, {
            "content": "② 相手の話の途中で話を始めるくせがあると、 人に言われてはじめて気がついた。",
            "hiragana": "",
            "meaning": "别人指出后我才意识到,我有在对方讲话中途插话的毛病。"
        }, {
            "content": "③ 山田先生の指導を受けてはじめて、 生物の観察が面白いと思うようになった。",
            "hiragana": "",
            "meaning": "得到山田老师的指导以后,我才开始觉得观察生物很有趣。"
        }, {
            "content": "④ チャンスがあってはじめて、才能が生きてくるのではないだろうか。",
            "hiragana": "",
            "meaning": "留有了机会以后,才能发挥出才干来,难道不是吗?"
        }],
        "usage": "動て形 + はじめて",
        "remark": """后续“新事情发生,觉察到、实现”等含义的句子。""",
        "source": "",
    },
    {
        "content": "〜上(で)",
        "hiragana": "〜うえ(で)",
        "meaning": """⇒準備としてまず〜してから、 その後で次に続く行動をする。
作准先做......, 其后再做接下来的行為。""",
        "example": [{
            "content": "① 文書が保存されていることを確かめた上で、パソコンをシャットダウンしてください。",
            "hiragana": "",
            "meaning": "请先确认文件已被保存之后再关电脑。"
        }, {
            "content": "② 経済的なことをよく考えた上で、 進路を決める必要がある。",
            "hiragana": "",
            "meaning": "留有必要在充分考虑经济因素之后,再决定今后的出路。"
        }, {
            "content": "③ 自分一人では決められませんので、 家族と相談した上で、お返事をいたします。",
            "hiragana": "",
            "meaning": "我一人无法决定,我会和家人商量之后再给您答复。"
        }, {
            "content": "④ この列車には特急券が必要です。 あらかじめ特急券をお買い求めの上、 ご乗車ください。",
            "hiragana": "",
            "meaning": "乘坐这趟列车需要用特快车票。请您事先买好特快车票再乘车。"
        }],
        "usage": "動 た形 + 上で / 名の + 上(で)",
        "remark": """前后句是同一主语。后续表示接着前面的动作结果而发生的人的意志性行为的句子。 前
接名詞肘有也用 「~上」形式,如例句 ④比「~上で」更加重。和「~てから」
一样,不用于前后动作以惯常的先后顺序发生的情况。""",
        "source": "",
    },
    {
        "content": "~次第",
        "hiragana": "~しだい",
        "meaning": """⇒ 〜が実現した後、 すぐに続けてある行動をする。硬い言い方
…………实现以后,马上采取后续行为。书面语。""",
        "example": [{
            "content": "① 詳しいことがわかり次第、ご連絡いたします。",
            "hiragana": "",
            "meaning": "事情一有进展,我会马上通知您。"
        }, {
            "content": "② 定員になり次第、締め切らせていただきます。",
            "hiragana": "",
            "meaning": "第一旦人数达到定额,便会截止报名。"
        }, {
            "content": "③ 会場の準備ができ次第、ご案内いたします。 もうしばらくお待ちください。",
            "hiragana": "",
            "meaning": "会场的准备工作一结束,我们会马上带大家过去。请再稍等片刻。"
        }],
        "usage": "ます + 次第",
        "remark": """前接表示“时间到了自然会发生”的事件实现瞬间的词语。后续表达说话人的希望、意
志,以及要求听话人做某事的句子。""",
        "source": "",
    },
    {
        "content": "~て以来てこのかた",
        "hiragana": "~ていらいてこのかた",
        "meaning": """⇒~してから今まで、ずっと同じ状態が続いている。
做…………之后直到现在,一直持续着相同的状态。""",
        "example": [{
            "content": "① 1年前にけがをして以来、体の調子がどうも良くない。",
            "hiragana": "",
            "meaning": "自从一年前受伤以来,身体状况一直不太好。"
        }, {
            "content": "② あの山の写真を見て以来、 いつかは登ってみたいとずっと思い続けてきた。",
            "hiragana": "",
            "meaning": "自从看了那座山的照片以后,一直想什么时候要爬一次。"
        }, {
            "content": "③ 子供が生まれて以来、外で酒を飲んでいない。",
            "hiragana": "",
            "meaning": "自从孩子出生以来,就没在外面喝过酒。"
        }, {
            "content": "④ 日本から帰国してこのかた、 毎日日本のことを思い出している。",
            "hiragana": "",
            "meaning": "民从日本回国以后,每天都在回忆日本生活的点点滴滴。"
        }, {
            "content": "⑤ 母がいなくなってこのかた、 母のことを考えない日はない。",
            "hiragana": "",
            "meaning": "自从母亲过世以后,没有一天不思念母亲。"
        }],
        "usage": "動て形 + 以来このかた",
        "remark": """前接表示过去某个时间点的词语,但不能是离现在很近的时间点。后续含有“一直持续
到现在”含义的句子。后面不能接表示将来的句子。""",
        "source": "",
    },
    {
        "content": "〜てからでないと~てからでなければ",
        "hiragana": "",
        "meaning": """⇒~した後でなければ、あることが実現しない。
如果不是做完……以后的话,某事就不会实现。""",
        "example": [{
            "content": "① この果物は赤くなってからでないと、酸っぱくて食べられません。",
            "hiragana": "",
            "meaning": "这种水果不变红的话,酸得没法吃。"
        }, {
            "content": "② もっと情報を集めてからでないと、 その話が本当かどうか判断できない。",
            "hiragana": "",
            "meaning": "如果不搜集更多信息的话,无法判断那件事是真是假。"
        }, {
            "content": "③ この電車は車内の清掃が済んでからでないと、 ご乗車になれません。",
            "hiragana": "",
            "meaning": "这辆车没有完成车内清扫的话,不能乘坐。"
        }, {
            "content": "④ 退院したばかりなんですから、十分に体力がついてからでなければ、 運動は無理ですよ。",
            "hiragana": "",
            "meaning": "留因为刚刚出院,如果没有恢复充足的体力的话,运动是不可能的。"
        }],
        "usage": "動 て形 + からでないとからでなければ",
        "remark": """后续表达否定含义的句子。""",
        "source": "",
    },
    {
        "content": "~をはじめ (として) ",
        "hiragana": "",
        "meaning": """⇒ 〜が代表例で、 そのほかにもいろいろある。硬い言い方
…………是有代表性的例子,除此以外还有很多其他的。书面语。""",
        "example": [{
            "content": "① この体育館では水泳をはじめ、いろいろなスポーツが楽しめる。",
            "hiragana": "",
            "meaning": "在这个体育馆里,能够享受到游泳等各种体育运动的乐趣。"
        }, {
            "content": "② 日本には 「桃太郎」 をはじめとして、 おじいさん、おばあさんが出てくる昔話が多い。",
            "hiragana": "",
            "meaning": "以《桃太郎》为代表,在日本有很多关于老爷爷,老奶奶的故事。"
        }, {
            "content": "③ このあたりには、市役所をはじめとする市の公共の建物が多い。",
            "hiragana": "",
            "meaning": "在这一带有许多像市政府这样的市级公共建筑物。"
        }],
        "usage": "名 + をはじめ (として) / 名 + をはじめとする + 名",
        "remark": """从许多事物中列举出有代表性的事物。后续表达包含有代表性的例子在内的多个事物的
词语。""",
        "source": "",
    },
    {
        "content": "〜からして",
        "hiragana": "",
        "meaning": """⇒ 〜という例一つを取ってもそうなのだから、 全体的にももちろんそうだ。
即使只抽取………..这一个例子都是这样的,所以整体来看也当然如此。""",
        "example": [{
            "content": "① この旅行の計画には無理がある。 出発時間からして早すぎる。",
            "hiragana": "",
            "meaning": "这个旅行计划有不可行之处。出发时间就过早了。"
        }, {
            "content": "② わたしはどうも猫が苦手だ。 あの光る目からして何となく怖い感じがする。",
            "hiragana": "",
            "meaning": "我很害怕猫。单是那双发光的眼睛就让人觉得很恐怖。"
        }, {
            "content": "③ わたしと夫とは似ているところが少ない。 第一、食べ物の好みからして正反対だ。",
            "hiragana": "",
            "meaning": "我和丈夫的相似点很少。首先单从食物的喜好上我俩就截然相反。"
        }, {
            "content": "④ さすがプロの選手は走り方からしてわたしたちとは違う。",
            "hiragana": "",
            "meaning": "不愧是职业运动员,单是跑步的姿势就和我们不一样。"
        }],
        "usage": "名 + からして",
        "remark": """把并非问题的本质,也并非重点的事情作为例子列举出来。后面多接消极评价的句子。""",
        "source": "",
    },
    {
        "content": "~にわたって",
        "hiragana": "",
        "meaning": """⇒ 〜の範囲全体にその状態が広がっている。
其状态扩大到……的全部。""",
        "example": [{
            "content": "① 連休の最終日、 高速道路は20キロにわたって渋滞が続いた。",
            "hiragana": "",
            "meaning": "长假的最后一天,高速公路上堵车长达20公里。"
        }, {
            "content": "② 彼はいろいろなジャンルにわたり、 たくさんの本を読んでいる。",
            "hiragana": "",
            "meaning": "民他读了很多书籍,广泛涉猎各种题材。"
        }, {
            "content": "③ 3日間にわたる研究発表大会が、 無事終了しました。",
            "hiragana": "",
            "meaning": "为期三天的研究发表大会圆满结束了。"
        }],
        "usage": "名 + にわたって / 名 + にわたる + 名",
        "remark": """前接表示场所、时间、次数、范围等幅度较大的词语。""",
        "source": "",
    },
    {
        "content": "~を通じて ・ ~を通して",
        "hiragana": "~をつうじて ・ ~をとおして",
        "meaning": """A 〜の期間ずっと同じ状態だ。
......的期間內一直保持同祥的状态。
B⇒ ~を手段にして、あることをする。
以……为手段做某事。
""",
        "example": [{
            "content": "① この町には四季を通じて観光客が訪れる。",
            "hiragana": "",
            "meaning": "这座城市一年四季都有游客来访。"
        }, {
            "content": "② 在職期間を通して皆様には大変お世話になりました。",
            "hiragana": "",
            "meaning": "在职期间承蒙大家多多关照。"
        }, {
            "content": "③ この10年間を通し、 彼はいつも新しいことに挑戦していた。",
            "hiragana": "",
            "meaning": "这十年间他总是在挑战新事物。"
        }, {
            "content": "④ 今日では、インターネットを通じて世界中の情報が手に入る。",
            "hiragana": "",
            "meaning": "译现在通过网络可以获得全球的信息。"
        }, {
            "content": "⑤ わたしたちは、ボランティア活動を通していろいろな国の人たちと交流を深めている。",
            "hiragana": "",
            "meaning": "我们通过志愿者活动和许多国家的人不断加深交流。"
        }],
        "usage": "",
        "remark": """A ......的期間內一直保持同祥的状态。
前接表示较长时间段的词语。后续表达持续性意义的句子。

B 以……为手段做某事。
前接词语不是直接的、具体的手段,而是中间媒介。
""",
        "source": "",
    },
    {
        "content": "~限り",
        "hiragana": "~かぎり",
        "meaning": """⇒ 〜の範囲は全部あることをする・ある状態だ。
在……的范围内全部做某事或是持续某种状态。""",
        "example": [{
            "content": "① 環境を守るためにわたしもできる限りのことをしたい。",
            "hiragana": "",
            "meaning": "为了保护环境,我也想做力所能及的事。"
        }, {
            "content": "② 君が知っている限りのことを全部わたしに話してほしい。",
            "hiragana": "",
            "meaning": "怪我希望你把知道的事情全部告訴我。"
        }, {
            "content": "③ あしたはいよいよ試合だ。 力の限り頑張ろう。",
            "hiragana": "",
            "meaning": "明天终于要比赛了。尽力而为吧。"
        }],
        "usage": "名-の・動 辞書形/ ている形 + 限り",
        "remark": """前接动词时,多使用「ている形」或是可能动词等。""",
        "source": "",
    },
    {
        "content": "〜だけ",
        "hiragana": "",
        "meaning": """⇒~の範囲の限界まであることをする。
把某事做到……的极限范围。""",
        "example": [{
            "content": "① ここにあるダンボールを、 車に積めるだけ積んで持って帰ってください。",
            "hiragana": "",
            "meaning": "请把这里的纸箱子,能装到车上的都装上,然后带回去。"
        }, {
            "content": "② 父は働くだけ働いて、 定年前に退職してしまった。",
            "hiragana": "",
            "meaning": "我的父亲一直拼命工作,在退休年龄前就离职了。"
        }, {
            "content": "③ 今日は部長に言いたいだけの不満を全部言って、すっきりした。",
            "hiragana": "",
            "meaning": "今天我把对部长的不满全部说了出来,心里痛快多了。"
        }, {
            "content": "④ バイキング形式の食事ですから、好きなものを好きなだけ取ってお召し上がりください。",
            "hiragana": "",
            "meaning": "因为是自助用餐,所以请喜欢吃什么就取什么来吃。"
        }],
        "usage": "動 辞書形 + だけ",
        "remark": """前面多接可能动词。不接表示瞬间完成意义的动词。前后使用同一个动词的情况较多。
也可以前接 「~たい・欲しい 好きな 必要な」 等詞語。""",
        "source": "",
    },
    {
        "content": "~に限り",
        "hiragana": "~にかぎり",
        "meaning": """⇒ ~だけは特別だ例外だ。 硬い言い方
仅限于………是特别的或例外的。书面语。""",
        "example": [{
            "content": "① このちらしをご持参のお客様に限り、 すべての商品を1割引でお買い求めいただけます。",
            "hiragana": "",
            "meaning": "仅限持有这种宣传单的顾客,可享受购买所有商品九折优惠。"
        }, {
            "content": "② 欠席理由が正当な場合に限り出席扱いにしますが、 それ以外の欠席は認めません。",
            "hiragana": "",
            "meaning": "只有缺席理由正当的情况可视为出席,除此以外的缺席都不予承认。"
        }, {
            "content": "③ この病院は午後6時までですが、 急を要する患者さんに限り、時間外でも診察いたします。",
            "hiragana": "",
            "meaning": "我们医院的就诊时间到下午6点,在工作时间以外我们只接急诊患者。"
        }],
        "usage": "名 + に限り",
        "remark": """用于向公众解释说明时的表达方式。前接表示被例外处理的事情的词语。后续表示仅适
用于该例外的句子。后面一般不接否定句和要求听话人做某事的句子。""",
        "source": "",
    },
    {
        "content": "~限り (は)",
        "hiragana": "~かぎり (は)",
        "meaning": """〜の状態が続いている間だけは、 同じ状態が続く。
只要持续......的状态,后项状态也同样持续。""",
        "example": [{
            "content": "① この町に住んでいる限り、 いつでも新鮮な食べ物が手に入る。 ここは野菜も魚も豊富だ。",
            "hiragana": "",
            "meaning": "只要住在这座城市,就能随时买到新鲜的食物。这里无论是蔬菜还是鱼品种都很丰富。"
        }, {
            "content": "② 社長が考え方を変えない限りは、この会社は何も変わらないのではないか。",
            "hiragana": "",
            "meaning": "只要社长不改变想法,这个公司就不会有任何改变,难道不是这样吗?"
        }, {
            "content": "③ 足が丈夫な限り、 まだまだ山登りが楽しめるだろう。",
            "hiragana": "",
            "meaning": "只要腿脚结实,就应该还能享受到登山的乐趣。"
        }, {
            "content": "④ 親である限りは、子供に対する責任があると思う。",
            "hiragana": "",
            "meaning": "我想只要身为父母,就要对孩子负责任。"
        }],
        "usage": "普通形現在(ナ形 だな/-である名だーである) +限り(は)",
        "remark": """前后都接表示状态的词语。因为是含有条件含义的句子,所以后面不接过去时态的句子。""",
        "source": "",
    },
    {
        "content": "~限りでは",
        "hiragana": "~かぎりでは",
        "meaning": """⇒情報源の範囲を〜だけにすると、 あることが言える。
把信息源的范围限定在......之内的话,就可以断言某种事情。""",
        "example": [{
            "content": "① 今回の調査の限りでは、書類にミスはなかった。",
            "hiragana": "",
            "meaning": "仅据本次调查显示,文件里没有错误。"
        }, {
            "content": "② ちょっと見た限りでは、 こちらの商品とあちらの商品では違いがないと思うのですが、 どうねだん ちがして値段が違うんですか。",
            "hiragana": "",
            "meaning": "据我粗略观察,感觉这件商品和那件商品没有差异,但为什么价格不同呢?"
        }, {
            "content": "③ わたしが知っている限りでは、この近所に花屋はありません。",
            "hiragana": "",
            "meaning": "据我所知,这附近没有花店。"
        }],
        "usage": "名の・动词辞書形 / た形/ ている形 +限りでは",
        "remark": """前接与荻得信息有美的同語 (「見る・聞く・覚えている・知っている・調査」等)。后
续表示某种判断或者公布某种信息的句子。""",
        "source": "",
    },
    {
        "content": "~に限って",
        "hiragana": "~にかぎって",
        "meaning": """A⇒ ~は普段と違っている。
...……与平日不同。

B⇒ 〜のことが、ほかの運が悪いことと偶然重なる。
.....这件事恰巧与其他的倒霉事赶到一起了。

C⇒ 特別に信じている〜 だから、悪いことはないはずだ。
因为特别相信…………,所以应该不会发生坏事。
""",
        "example": [{
            "content": "① ふだん酒などあまり飲まない彼が、 今日に限ってかなり飲んだ。 何かあったのだろうか。",
            "hiragana": "",
            "meaning": "平日不太喝酒的他今天却喝了很多。是不是出什么事了。"
        }, {
            "content": "② わたしはいつもは駅前で買い物するのだが、 その日に限って車で遠くのスーパーまで行った。",
            "hiragana": "",
            "meaning": "我总是在车站附近买东西,但就那一天开车去了很远的超市。"
        }, {
            "content": "③ どうしてあの日に限って別の道を通ろうと思ったのか、 思い出せない。",
            "hiragana": "",
            "meaning": "我想不起来为什么就那天要从另外一条路走呢。"
        }, {
            "content": "④ 庭の手入れをしようと思っている日に限って雨が降る。",
            "hiragana": "",
            "meaning": "偏偏在我想要修整院子的时候下雨。"
        }, {
            "content": "⑤ 今日は大切な用事があったのに、こんな時に限って子供が熱を出してしまった。",
            "hiragana": "",
            "meaning": "今天有重要的事情要办,但偏偏这个时候孩子发烧了。"
        }, {
            "content": "⑥ うちの子に限って友達をいじめることはないと思いますがとても優しい子なんですよ。",
            "hiragana": "",
            "meaning": "我想我家孩子是绝不会欺负小朋友的......他是个非常善良的孩子。"
        }, {
            "content": "⑦ あのレストランに限って古い食材など使うはずはないと思っていたのに･･････。",
            "hiragana": "",
            "meaning": "我以前一直认为,那家餐厅的话是不可能用一些不新鲜的食材的,但是没想到…………"
        }],
        "usage": """名 + に限って""",
        "remark": """A ...……与平日不同。
后续表达“与平日不同,很特别”这种含义的句子。

B .....这件事恰巧与其他的倒霉事赶到一起了。
后续表达“变成不好的状况”这种含义的句子。整体来看表达了说话人的不满。

C 因为特别相信…………,所以应该不会发生坏事。
后续“应该不会变成坏的状况”这种含义的否定句,来表达说话人的判断。
""",
        "source": "",
    },
    {
        "content": "~に限らず",
        "hiragana": "~にかぎらず",
        "meaning": """⇒範囲は~だけでなく、 さらに広い範囲のものも含む。
范围不限于….....,逐包含同一美的更广的范围。""",
        "example": [{
            "content": "① この記念館は、休日に限らず一年中 入館者が多い。",
            "hiragana": "",
            "meaning": "留这个纪念馆,不仅仅是节假日的时候,全年的入馆人数都很多。"
        }, {
            "content": "② うちに限らず近所の住民はみんな夜中のバイクの音に悩まされている。",
            "hiragana": "",
            "meaning": "不光是我家,附近的居民都对深夜里的摩托车噪音感到困扰。"
        }, {
            "content": "③ 近年、地方の町に限らず大都会でも書店の閉店が相次いでいる。",
            "hiragana": "",
            "meaning": "隔近年来,不光是地方的小城市,就连大城市的书店也相继关门停业。"
        }],
        "usage": "名 +に限らず",
        "remark": """后续句子中多包含表示“其他也”含义的「も」,或者表示更广范围的词语(「みんな・さまざまな・いつも」等)。""",
        "source": "",
    },
    {
        "content": "〜のみならず",
        "hiragana": "",
        "meaning": """⇒ 〜だけでなく、ほかにもある。硬い言い方
不仅……,此外还有其他的。书面语。""",
        "example": [{
            "content": "① 電気代のみならず、 ガス代や水道代も値上がりするようだ。",
            "hiragana": "",
            "meaning": "不仅仅是电费,好像煤气费、水费等也都要涨价。"
        }, {
            "content": "② 与党のみならず、 野党も党首の選出には慎重だ。",
            "hiragana": "",
            "meaning": "不仅仅是执政党,在野党的党首选举也很慎重。"
        }, {
            "content": "③ 石井さんは、差別的な発言をしたのみならず、 それについて謝ることもなかった。",
            "hiragana": "",
            "meaning": "石井非但做了歧视性的发言,而且也没就此道歉。"
        }],
        "usage": "名・普通形(ナ形 だーである・名だーである) +のみならず",
        "remark": """不同于「~に限らず」,也可以用于同等級的其他事物也一祥的情況。后面多是含有“其他也”含义的使用「も」的句子。""",
        "source": "",
    },
    {
        "content": "〜ばかりか",
        "hiragana": "",
        "meaning": """⇒ 〜だけでも十分なのに、 さらにほかのことも加わる。
仅仅……就足够了,但还追加了其他的事情。""",
        "example": [{
            "content": "① 発見が遅れたばかりか対策にも手間取ったので、牛の病気が広がってしまった。",
            "hiragana": "",
            "meaning": "不仅发现晚了,而且制订对策也花费了时间,所以牛的疫情就扩散了。"
        }, {
            "content": "② 田島先生の説明は、子供にもわかりやすいばかりか、 非常におもしろくてためになる。",
            "hiragana": "",
            "meaning": "田岛老师的讲解不仅让孩子容易理解,而且还非常有趣,真是受益匪浅。"
        }, {
            "content": "③ Aコースの山道は、 初心者には危険なばかりか、途中の景色もあまり良くない。",
            "hiragana": "",
            "meaning": "通路线A的山路,不仅对于初学者而言很危险,而且沿途的景色也不怎么好。"
        }, {
            "content": "④ 友達ばかりか親兄弟も彼の居場所を知らない。",
            "hiragana": "",
            "meaning": "不仅朋友,就连他的父母兄弟姐妹也不知道他的住处。"
        }],
        "usage": "名・普通形(形 だ -な/-である・ 名 だーである) +ばかりか",
        "remark": """前句叙述不寻常的事情,后句再次追加使人感到意外的其他事情。后句多使用表达“其他也”含义的「も」。后面不接要求听话人做某事的句子。""",
        "source": "",
    },
    {
        "content": "〜はもとより",
        "hiragana": "",
        "meaning": """⇒ 〜はもちろん、 ほかもそうだ。 硬い言い方
・自不必説,其他也如此。书面語。""",
        "example": [{
            "content": "① たばこは本人はもとより、周りの人にも害を及ぼす。",
            "hiragana": "",
            "meaning": "吸烟对于吸烟者本人自不必说,对于周围的人也会产生危害。"
        }, {
            "content": "② 家族で外国に滞在している人は、自分の健康管理はもとより家族の心身の健康にも気を配ったほうがいい全家生活在国外的人,照顾好自己的身体健康自不用说,还要留意家人的身心健康。",
            "hiragana": "",
            "meaning": "じもと じゅうみん"
        }, {
            "content": "③ 地元の住民はもとより、 周辺の地域に住む人たちも原子力発電所に不安を感じている。",
            "hiragana": "",
            "meaning": "当地居民自不用说,居住在周边地区的人们也对核电站感到不安。"
        }, {
            "content": "④ この学校では、教室内ではもとより教室の外でも禁煙を守ってください。",
            "hiragana": "",
            "meaning": "在本校,教室内自不用说了,教室外也严禁吸烟。"
        }],
        "usage": "名詞(+助词) +はもとより",
        "remark": """前接表达说话人认为理所当然的例子的词语。后续其他的例子。后面多接表达“其他”含义的「も」的句子。""",
        "source": "",
    },
    {
        "content": "〜上(に)",
        "hiragana": "〜うえ(に)",
        "meaning": """⇒ ~だけでなく、 さらにいいこと悪いことが重なる。
不......,而且追加更好或更坏的事情。""",
        "example": [{
            "content": "① 田中さんには仕事を手伝ってもらった上に、 仕事の後、 ごちそうになった。",
            "hiragana": "",
            "meaning": "田中不仅在工作上帮助我,而且工作结束后还请我吃了饭。"
        }, {
            "content": "② 森田先生は、毎日医師として忙しく仕事をしている上、週末も学会や講演で飛び回っている。",
            "hiragana": "",
            "meaning": "森田医生不仅每天忙着为患者治病,周末还要四处奔走参加学术会议和演讲等。"
        }, {
            "content": "③ このテキストは用語が難しい上に、 内容も良くない。",
            "hiragana": "",
            "meaning": "这本教材不仅用词难懂,而且内容也不好。"
        }, {
            "content": "④ ここは空気がきれいな上、 近くに明るいところがないので星がよく見える。",
            "hiragana": "",
            "meaning": "这里不仅空气清新,而且附近没有灯火明亮的建筑物,所以能很清楚地看见星星。"
        }, {
            "content": "⑤ 今日は寝不足の上、 少し熱がある。 早く帰りたい。",
            "hiragana": "",
            "meaning": "今天不仅睡眠不足,而且还有点儿发烧。想早点儿回家。"
        }],
        "usage": "普通形(ナ形だな/-である・名だーの/-である) +上(に)",
        "remark": """前后句是相同评价的词语(正面评价搭配正面评价,负面评价搭配负面评价)。不接相
反的事情或者没有关系的事情。后面不接要求听话人做某事的句子。""",
        "source": "",
    },
]

if __name__ == '__main__':
    df = pd.DataFrame(grammars)
    df["id"] = df.index
    df = df.reindex(["id", "content", "hiragana", "meaning", "usage", "example", "remark", "source"], axis=1)
    with open("grammar.json", "w", encoding="utf-8") as fp:
        df.to_json(fp, orient="records", indent=4, force_ascii=False)
