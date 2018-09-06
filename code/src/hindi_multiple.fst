$ladakI-morph$ = "../src/ladakI-paradigm.lex" <Noun>:<> ({<singular><direct>}:{} | {<singular><oblique>}:{} |{<plural><direct>}:{yAM} | {<plural><oblique>}:{yoM})
$ladak-morph$ = "../src/ladakA-paradigm.lex" <Noun>:<> ({<singular><direct>}:{} | {<singular><oblique>}:{e} |{<plural><direct>}:{e} | {<plural><oblique>}:{oM})
$morph$ = $ladakI-morph$ | $ladak-morph$
ALPHABET = [A-Za-z] [<Noun> I yAM yoM]:i
$delete-I$ = [yAM yoM] <=> i (<Noun>i:<>[yAM yoM])
ALPHABET = [A-Za-z] [<Noun> A e oM]:<>
$delete-A$ = [e oM] <=> <> (<Noun>:<>[e oM]) 
$delete$ = $delete-I$ || $delete-A$
$morph$ || $delete$ 

