from nltk.translate.bleu_score import sentence_bleu
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def calculate_similarity(X, Y):
    X = X.lower()
    Y = Y.lower()

    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    sw = stopwords.words('english')
    l1 = []
    l2 = []

    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    return cosine


reference1 = "TimeWarner said fourth quarter sales rose 2% to $11.1bn from $10.9bn.For the full-year, TimeWarner " \
             "posted a profit of $3.36bn, up 27% from its 2003 performance, while revenues grew 6.4% to " \
             "$42.09bn.Quarterly profits at US media giant TimeWarner jumped 76% to $1.13bn (£600m) for the three " \
             "months to December, from $639m year-earlier.However, the company said AOL's underlying profit before " \
             "exceptional items rose 8% on the back of stronger internet advertising revenues.Its profits were buoyed " \
             "by one-off gains which offset a profit dip at Warner Bros, and less users for AOL.For 2005, TimeWarner " \
             "is projecting operating earnings growth of around 5%, and also expects higher revenue and wider profit " \
             "margins.It lost 464,000 subscribers in the fourth quarter profits were lower than in the preceding " \
             "three quarters.Time Warner's fourth quarter profits were slightly better than analysts' expectations. "
candidate_bert1 = "Ad sales boost Time Warner profit Quarterly profits at US media giant TimeWarner jumped 76% to " \
                  "$1.13bn (Â£600m) for the three months to December, from $639m year-earlier. It lost 464," \
                  "000 subscribers in the fourth quarter profits were lower than in the preceding three quarters. " \
                  "Time Warner's fourth quarter profits were slightly better than analysts' expectations. The " \
                  "company said it was unable to estimate the amount it needed to set aside for legal reserves, " \
                  "which it previously set at $500m. It intends to adjust the way it accounts for a deal with German " \
                  "music publisher Bertelsmann's purchase of a stake in AOL Europe, which it had reported as " \
                  "advertising revenue. "
print('BLEU score of BERT of text 1 -> {}'.format(sentence_bleu(reference1, candidate_bert1)))
candidate_sumy1 = "Ad sales boost Time Warner profit.TimeWarner said fourth quarter sales rose 2% to $11.1bn from " \
                  "$10.9bn.TimeWarner also has to restate 2000 and 2003 results following a probe by the US " \
                  "Securities Exchange Commission (SEC), which is close to concluding.Time Warner's fourth quarter " \
                  "profits were slightly better than analysts' expectations.For the full-year, TimeWarner posted a " \
                  "profit of $3.36bn, up 27% from its 2003 performance, while revenues grew 6.4% to $42.09bn.It " \
                  "intends to adjust the way it accounts for a deal with German music publisher Bertelsmann's " \
                  "purchase of a stake in AOL Europe, which it had reported as advertising revenue. "
print('BLEU score of SUMY of text 1 -> {}'.format(sentence_bleu(reference1, candidate_sumy1)))
candidate_xlnet1 = "Ad sales boost Time Warner profit.Quarterly profits at US media giant TimeWarner jumped 76% to " \
                   "$1.13bn (Â£600m) for the three months to December, from $639m year-earlier. Its profits were " \
                   "buoyed by one-off gains which offset a profit dip at Warner Bros, and less users for AOL. Time " \
                   "Warner's fourth quarter profits were slightly better than analysts' expectations. For 2005, " \
                   "TimeWarner is projecting operating earnings growth of around 5%, and also expects higher revenue " \
                   "and wider profit margins. "
print('BLEU score of XLNET of text 1 -> {}'.format(sentence_bleu(reference1, candidate_xlnet1)))
print('Similarity score of text 1 using BERT is: ', calculate_similarity(reference1, candidate_bert1))
print('Similarity score of text 1 using SUMY is: ', calculate_similarity(reference1, candidate_sumy1))
print('Similarity score of text 1 using XLNET is: ', calculate_similarity(reference1, candidate_xlnet1))
print("\n\n")

reference2 = "Bloom is to be formally presented with the Hans Christian Andersen Award this spring in Anderson's " \
             "hometown of Odense.Later at a gala dinner, Danish supermodel Helena Christensen was named a Hans " \
             "Christian Andersen ambassador.French musician Jean-Michel Jarre is to perform at a concert in " \
             "Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen.\"Christian " \
             "Andersen's fairy tales are timeless and universal,\" said Jarre.The royal couple also visited the Hans " \
             "Christian Anderson School complex, where Queen Mary read The Ugly Duckling to the young " \
             "audience.\"Bloom recognizes the darker aspects of Andersen's authorship,\" Prince Frederik said. "
candidate_bert2 = "Jarre joins fairytale celebration French musician Jean-Michel Jarre is to perform at a concert in " \
                  "Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen. Denmark is " \
                  "holding a three-day celebration of the life of the fairy-tale author, with a concert at Parken " \
                  "stadium on 2 April. Denmark's Crown Prince Frederik and Crown Princess Mary visited New York on " \
                  "Monday to help promote the festivities. "
print('BLEU score of BERT of text 2 -> {}'.format(sentence_bleu(reference2, candidate_bert2)))
candidate_sumy2 = "Jarre joins fairytale celebration French musician Jean-Michel Jarre is to perform at a concert in " \
                  "Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen.Denmark is " \
                  "holding a three-day celebration of the life of the fairy-tale author, with a concert at Parken " \
                  "stadium on 2 April.Other stars are expected to join the line-up in the coming months, " \
                  "and the Danish royal family will attend.There are year-long celebrations planned across the world " \
                  "to celebrate Andersen and his work, which includes The Emperor's New Clothes and The Little " \
                  "Mermaid.\"Bloom recognizes the darker aspects of Andersen's authorship,\" Prince Frederik said. "
print('BLEU score of SUMY of text 2 -> {}'.format(sentence_bleu(reference2, candidate_sumy2)))
candidate_xlnet2 = "Jarre joins fairytale celebration.French musician Jean-Michel Jarre is to perform at a concert in " \
                   "Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen. Denmark is " \
                   "holding a three-day celebration of the life of the fairy-tale author, with a concert at Parken " \
                   "stadium on 2 April. The pair were at a Manhattan library to honour US literary critic Harold " \
                   "Bloom \"the international icon we thought we knew so well\". "
print('BLEU score of XLNET of text 2 -> {}'.format(sentence_bleu(reference2, candidate_xlnet2)))
print('Similarity score of text 2 using BERT is: ', calculate_similarity(reference2, candidate_bert2))
print('Similarity score of text 2 using SUMY is: ', calculate_similarity(reference2, candidate_sumy2))
print('Similarity score of text 2 using XLNET is: ', calculate_similarity(reference2, candidate_xlnet2))
print("\n\n")

reference3 = "Ms Hewitt also announced a new drive to help women who want to work in male dominated sectors, " \
             "saying sexism at work was still preventing women reaching their full potential.\"But it is also about " \
             "saying childcare jobs are really there for women and not suitable for men.Earlier, she told BBC Radio " \
             "4's Today programme: \"What we are talking about here is the fact that about six out of 20 women work " \
             "in jobs that are low-paid and typically dominated by women, so we have got very segregated " \
             "employment.Women in full-time work earn 19% less than men, according to the Equal Opportunities " \
             "Commission (EOC).The minister told delegates that getting rid of \"career sexism\" was vital to closing " \
             "the gender pay gap.\"Career sexism limits opportunities for women of all ages and prevents them from " \
             "achieving their full potential.\"Career sexism is about saying that engineering, for instance, " \
             "where only 10% of employees are women, is really a male-dominated industry.Plans include funding for " \
             "universities to help female science and engineering graduates find jobs and \"taster courses\" for men " \
             "and women in non-traditional jobs.Plans to extend paid maternity leave beyond six months should be " \
             "prominent in Labour's election manifesto, the Trade and Industry Secretary has said.\"The average woman " \
             "working full-time is being paid about 80p for every pound a man is earning.For women working part-time " \
             "it is 60p. "
candidate_bert3 = "Hewitt decries 'career sexism'Plans to extend paid maternity leave beyond six months should be " \
                  "prominent in Labour's election manifesto, the Trade and Industry Secretary has said. Mothers can " \
                  "currently take up to six months' paid leave - and six unpaid. Women in full-time work earn 19% " \
                  "less than men, according to the Equal Opportunities Commission (EOC). Career sexism is about " \
                  "saying that engineering, for instance, where only 10% of employees are women, is really a " \
                  "male-dominated industry. Research conducted by the EOC last year revealed that many Britons " \
                  "believe the pay gap between men and women is the result of \"natural differences\" between the " \
                  "sexes. "
print('BLEU score of BERT of text 3 -> {}'.format(sentence_bleu(reference3, candidate_bert3)))
candidate_sumy3 = "Ms Hewitt was speaking at a gender and productivity seminar organised by the Equal Opportunities " \
                  "Commission (EOC).Ms Hewitt told the seminar: \"Clearly, one of the things we need to do in the " \
                  "future is to extend the period of payment for maternity leave beyond the first six months into the " \
                  "second six months.Ms Hewitt also announced a new drive to help women who want to work in male " \
                  "dominated sectors, saying sexism at work was still preventing women reaching their full " \
                  "potential.The minister told delegates that getting rid of \"career sexism\" was vital to closing " \
                  "the gender pay gap.\"Career sexism is about saying that engineering, for instance, where only 10% " \
                  "of employees are women, is really a male-dominated industry.\"But it is also about saying " \
                  "childcare jobs are really there for women and not suitable for men. "
print('BLEU score of SUMY of text 3 -> {}'.format(sentence_bleu(reference3, candidate_sumy3)))
candidate_xlnet3 = "Hewitt decries 'career sexism'.Plans to extend paid maternity leave beyond six months should be " \
                   "prominent in Labour's election manifesto, the Trade and Industry Secretary has said. The minister " \
                   "told delegates that getting rid of \"career sexism\" was vital to closing the gender pay gap. " \
                   "Earlier, she told BBC Radio 4's Today programme: \"What we are talking about here is the fact " \
                   "that about six out of 20 women work in jobs that are low-paid and typically dominated by women, " \
                   "so we have got very segregated employment. \" Research conducted by the EOC last year revealed " \
                   "that many Britons believe the pay gap between men and women is the result of \"natural " \
                   "differences\" between the sexes. And retired women have just over half the income of their male " \
                   "counterparts on average. "
print('BLEU score of XLNET of text 3 -> {}'.format(sentence_bleu(reference3, candidate_xlnet3)))
print('Similarity score of text 3 using BERT is: ', calculate_similarity(reference3, candidate_bert3))
print('Similarity score of text 3 using SUMY is: ', calculate_similarity(reference3, candidate_sumy3))
print('Similarity score of text 3 using XLNET is: ', calculate_similarity(reference3, candidate_xlnet3))
print("\n\n")

reference4 = "I am very happy to see you all, members of the athletics family, respond positively to the IAAF call to " \
             "sit together and discuss what more we can do in the fight against doping,\" said Diack.The two task " \
             "forces will report back to the IAAF Council, at its April meeting in Qatar.\"Nothing was decided to " \
             "change things - it was more to have a forum of the stakeholders allowing them to express themselves," \
             "\" said an IAAF spokesman.The IAAF - athletics' world governing body - has met anti-doping officials, " \
             "coaches and athletes to co-ordinate the fight against drugs in sport. "
candidate_bert4 = "IAAF launches fight against drugs.The IAAF - athletics' world governing body - has met anti-doping " \
                  "officials, coaches and athletes to co-ordinate the fight against drugs in sport. It was also " \
                  "agreed that a programme to \"de-mystify\" the issue to athletes, the public and the media was a " \
                  "priority. "
print('BLEU score of BERT of text 4 -> {}'.format(sentence_bleu(reference4, candidate_bert4)))
candidate_sumy4 = "IAAF launches fight against drugs.The IAAF - athletics' world governing body - has met anti-doping " \
                  "officials, coaches and athletes to co-ordinate the fight against drugs in sport.Two task forces " \
                  "have been set up to examine doping and nutrition issues.It was also agreed that a programme to " \
                  "\"de-mystify\" the issue to athletes, the public and the media was a priority.\"Nothing was " \
                  "decided to change things - it was more to have a forum of the stakeholders allowing them to " \
                  "express themselves,\" said an IAAF spokesman.\"Getting everyone together gave us a lot of food for " \
                  "thought. "
print('BLEU score of SUMY of text 4 -> {}'.format(sentence_bleu(reference4, candidate_sumy4)))
candidate_xlnet4 = "IAAF launches fight against drugs.The IAAF - athletics' world governing body - has met " \
                   "anti-doping officials, coaches and athletes to co-ordinate the fight against drugs in sport. " \
                   "Nothing was decided to change things - it was more to have a forum of the stakeholders allowing " \
                   "them to express themselves,\" said an IAAF spokesman. \" "
print('BLEU score of XLNET of text 4 -> {}'.format(sentence_bleu(reference4, candidate_xlnet4)))
print('Similarity score of text 4 using BERT is: ', calculate_similarity(reference4, candidate_bert4))
print('Similarity score of text 4 using SUMY is: ', calculate_similarity(reference4, candidate_sumy4))
print('Similarity score of text 4 using XLNET is: ', calculate_similarity(reference4, candidate_xlnet4))
print("\n\n")

reference5 = "\"We are hoping to understand the creative industry that has a natural thirst for broadband technology," \
             "\" said Frank Stone, head of the BT's business sector programmes.The art world is \"fantastically " \
             "rich\", said Mr Stone, with creative people and ideas which means traditional companies like BT want to " \
             "get in with them.The partnership between artists and technologists is part of trying to understand the " \
             "creative potential of technologies like broadband net, according to Mr Stone.The idea, says BT, " \
             "is to shape a \"21st Century model\" which will help cement the art, technology, and business worlds " \
             "together.It is about both industries borrowing strategies and creative ideas together which can result " \
             "in better business practices for creative industries, or more patent ideas for tech " \
             "companies.Technology as a way of unleashing creativity has massive potential, not least because it " \
             "gives people something to do with their technology.BT's own engine, Tara (Total Abstract Rendering " \
             "Architecture) has been in development since 2001 and has been used to recreate virtual interactive " \
             "models of buildings for planners.But collaboration between art and digital technology is by no means " \
             "new, and many keen coders, designers, games makers and animators argue that what they create is art " \
             "itself.The hi-tech and the arts worlds have for some time danced around each other and offered creative " \
             "and technical help when required.They have both been created using the telco's technology that it has " \
             "been incubating at its research and development arm, including a sophisticated graphics rendering " \
             "program.But that dance is growing more intimate as hi-tech firms look to the creative industries for " \
             "inspiration.UK telco BT is serious about the idea and has launched its Connected World " \
             "initiative.Between 1997 and 2002, the creative industry brought £21 billion to London alone.He looks " \
             "after several \"centres of excellence\" which the telco has set up with other institutions and " \
             "organisations, one of which is focused on creative industries.In their previous works they used the " \
             "Quake game graphics engine. "
candidate_bert5 = "Technology gets the creative bug.The hi-tech and the arts worlds have for some time danced around " \
                  "each other and offered creative and technical help when required. The idea, says BT, is to shape a " \
                  "\"21st Century model\" which will help cement the art, technology, and business worlds together. " \
                  "\" To mark the initiative's launch, a major international art installation is to open on 15 April " \
                  "in Brussels, with a further exhibit in Madrid later in the summer. The river was integral to the " \
                  "city's survival for hundreds of years and it was equally essential to the city that it " \
                  "disappeared,\" said the artists. \" Technology as a way of unleashing creativity has massive " \
                  "potential, not least because it gives people something to do with their technology. It is about " \
                  "how can everyone have the best seat in house and asking if technology has a role in solving that " \
                  "problem.\" With broadband penetration reaching 100% in the UK, businesses with a stake in the " \
                  "technology want to give people reasons to want and use it. "
print('BLEU score of BERT of text 5 -> {}'.format(sentence_bleu(reference5, candidate_bert5)))
candidate_sumy5 = "The idea, says BT, is to shape a \"21st Century model\" which will help cement the art, " \
                  "technology, and business worlds together.\"We are hoping to understand the creative industry that " \
                  "has a natural thirst for broadband technology,\" said Frank Stone, head of the BT's business " \
                  "sector programmes.BT's own engine, Tara (Total Abstract Rendering Architecture) has been in " \
                  "development since 2001 and has been used to recreate virtual interactive models of buildings for " \
                  "planners.It was also used in 2003 in Encounter, an urban-based, pervasive game that combined both " \
                  "virtual play in conjunction with physical, on-the-street action.The art world is \"fantastically " \
                  "rich\", said Mr Stone, with creative people and ideas which means traditional companies like BT " \
                  "want to get in with them.It is an industry that is growing by 6% a year too. "
print('BLEU score of SUMY of text 5 -> {}'.format(sentence_bleu(reference5, candidate_sumy5)))
candidate_xlnet5 = "Technology gets the creative bug.The hi-tech and the arts worlds have for some time danced around " \
                   "each other and offered creative and technical help when required. Often this help has come in the " \
                   "form of corporate art sponsorship or infrastructure provision. To mark the initiative's launch, " \
                   "a major international art installation is to open on 15 April in Brussels, with a further exhibit " \
                   "in Madrid later in the summer. In their previous works they used the Quake game graphics engine. " \
                   "Because the artists wanted video and interactive elements in their worlds, new features were " \
                   "added to Tara in order to handle the complex data sets. Between 1997 and 2002, the creative " \
                   "industry brought Â£21 billion to London alone. The partnership between artists and technologists " \
                   "is part of trying to understand the creative potential of technologies like broadband net, " \
                   "according to Mr Stone. "
print('BLEU score of XLNET of text 5 -> {}'.format(sentence_bleu(reference5, candidate_xlnet5)))
print('Similarity score of text 5 using BERT is: ', calculate_similarity(reference5, candidate_bert5))
print('Similarity score of text 5 using SUMY is: ', calculate_similarity(reference5, candidate_sumy5))
print('Similarity score of text 5 using XLNET is: ', calculate_similarity(reference5, candidate_xlnet5))
print("\n\n")
