messages = [
    {
        "role": "system", 
        "content": "You will help me parse raw noisy OCR output into neat tables. The output should contain the proper Odia characters instead of escape sequences."
    },
    {
        "role": "user", 
        "content": """which of these are odia characters:

['\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', 'é', 'ā', 'ļ', 'Ľ', 'Ŀ', 'ŀ', 'Ł', 'ł', 'Ń', 'Ņ', 'Ň', 'ň', 'Ŋ', 'ŋ', 'Ŏ', 'ŏ', 'Ő', 'ő', 'Œ', 'Ŕ', 'ŕ', 'ŗ', 'Ř', 'ř', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Š', 'š', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'Ű', 'ŵ', 'Ŷ', 'ŷ', 'Ÿ', 'Ź', 'Ż', 'ż', 'Ž', 'ſ', 'Ɓ', 'Ƃ', 'ƃ', 'Ƅ', 'ƅ', 'Ɔ', 'ƈ', 'Ɗ', 'ƌ', 'ƍ', 'Ǝ', 'Ə', 'Ɛ', 'Ƒ', 'ƒ', 'Ɠ', 'Ɣ', 'ƕ', 'Ɩ', 'Ɨ', 'Ƙ', 'ƙ', 'ƚ', 'ƛ', 'Ɲ', 'Ɵ', 'ơ', 'Ƣ', 'Ƥ', 'ƥ', 'Ʀ', 'Ƨ', 'ƨ', 'Ʃ', 'ƪ', 'ƫ', 'Ƭ', 'ƭ', 'Ʈ', 'Ư', 'ư', 'Ʊ', 'Ʋ', 'Ƴ', 'Ƶ', 'ƶ', 'Ʒ', 'Ƹ', 'ƹ', 'ƺ', 'ƻ', 'Ƽ', 'ƽ', 'ƿ', 'ǀ', 'ǂ', 'ǃ', 'ǅ', 'ǆ', 'Ǉ', 'ǉ', 'ǋ', 'ǌ', 'Ǎ', 'ǎ', 'ǐ', 'Ǒ', 'Ǔ', 'Ǖ', 'ǘ', 'Ǚ', 'ǚ', 'ǜ', 'ǝ', 'Ǟ', 'ǟ', 'Ǡ', 'ǡ', 'ǣ', 'Ǥ', 'ǥ', 'ǧ', 'Ǩ', 'ǩ', 'ǫ', 'ǰ', 'Ǳ', 'ǲ', 'ǳ', 'Ƿ', 'Ǻ', 'Ǽ', 'ǿ', 'ȁ', 'Ȅ', 'ȅ', 'Ȇ', 'ȇ', 'Ȉ', 'Ȏ', 'Ȑ', 'ȑ', 'ȡ', 'ȣ', 'ȥ', 'Ȧ', 'Ȫ', 'ȫ', 'ȯ', 'ȱ', 'Ȳ', 'ȳ', 'ȴ', 'ȷ', 'Ȼ', 'ə', 'ɚ', 'ɜ', 'ɰ', 'ɲ', '।', 'ଁ', 'ଂ', 'ଃ', 'ଅ', 'ଆ', 'ଇ', 'ଈ', 'ଉ', 'ଊ', 'ଋ', 'ଏ', 'ଐ', 'ଓ', 'ଔ', 'କ', 'ଖ', ''ଗ', 'ଘ', 'ଙ', 'ଚ', 'ଛ', 'ଜ', 'ଝ', 'ଟ', 'ଠ', 'ଡ', 'ଢ', 'ଣ', 'ତ', 'ଥ', 'ଦ', 'ଧ', 'ନ', 'ପ', 'ଫ', 'ବ', 'ଭ', 'ମ', 'ଯ', 'ର', 'ଲ', 'ଳ', 'ଶ', 'ଷ', 'ସ', 'ହ', 'ା', 'ି', 'ୀ', 'ୁ', 'ୂ', 'ୃ', 'େ', '୍', 'ୖ', 'ୗ', 'ଡ଼', 'ଢ଼', 'ୟ', '୦', '୧', '୨', '୩', '୪', '୫', '୬', '୭', '୮', '୯', 'ṣ', '–', '‘', '’', '“', '”', '…', '     '\uf0b7']"""
    },
    {
        "role": "assistant",
        "content": """From the list you provided, the characters that are part of the Odia lexicon are:

ଅ, ଆ, ଇ, ଈ, ଉ, ଊ, ଋ, ଏ, ଐ, ଓ, ଔ, କ, ଖ, ଗ, ଘ, ଙ, ଚ, ଛ, ଜ, ଝ, ଟ, ଠ, ଡ, ଢ, ଣ, ତ, ଥ, ଦ, ଧ, ନ, ପ, ଫ, ବ, ଭ, ମ, ଯ, ର, ଲ, ଳ, ଶ, ଷ, ସ, ହ, ା, ି, ୀ, ୁ, ୂ, ୃ, େ, ୍, ୖ, ୗ, ଡ଼, ଢ଼, ୟ, ୦, ୧, ୨, ୩, ୪, ୫, ୬, ୭, ୮, ୯

Please note that some characters in the list you provided may not be recognizable Odia characters or may have been garbled in the representation. I have excluded those characters from the Odia lexicon."""
    },
    {
        "role": "user",
        "content": """Replace the garbled characters in the text I provide below, with the appropriate odia letters. the replacements will probably NOT be a part of this list: ଅ, ଆ, ଇ, ଈ, ଉ, ଊ, ଋ, ଏ, ଐ, ଓ, ଔ, କ, ଖ, ଗ, ଘ, ଙ, ଚ, ଛ, ଜ, ଝ, ଟ, ଠ, ଡ, ଢ, ଣ, ତ, ଥ, ଦ, ଧ, ନ, ପ, ଫ, ବ, ଭ, ମ, ଯ, ର, ଲ, ଳ, ଶ, ଷ, ସ, ହ, ା, ି, ୀ, ୁ, ୂ, ୃ, େ, ୍, ୖ, ୗ, ଡ଼, ଢ଼, ୟ, ୦, ୧, ୨, ୩, ୪, ୫, ୬, ୭, ୮, ୯

1 A class  : 1. Ȅଥମ  େȎଣୀ , କ’ େȎଣୀ , 2. ଅତି ଭଲ 
 ~ prisoner : Ȅଥମ  େȎଣୀ  ବƃୀ / କଏଦି 
a priori  (a) : 1. ସହଜ ଉପଲƒ , 2. ପୂବƽ ସିŶ, 3. ସହଜ 
ଅନୁେମୟ  
ab ante  : ପୂବƽର ୁ  
ab extra  : ବାହȻତଃ  
ab initio  : ଆରƗର ୁ  
ab initio mundi  : ସୃƨି ଆରƗର ୁ , ମୂଳର ୁ  
ab invito  : ଅନିŒାର ୁ  
ab judicatio  : ନȻାୟାଳୟର ୁ  
abandon  (v) : ପରିତȻାଗ  କରିବା , ବଜƽନ କରିବା  (to 
abandon the flood -affected mines)  
abandoned  (a) : ପରିତȻĽ , ବଜƽନ କରାଯାଇǆବା  (a 
list of the abandoned assets of all 
departments)  
abandonment  (n) : ପରିତȻାଗ , ବଜƽନ 
(abandonment of the unsafe buildings)  
abate  (v) : 1.ଦୂର କରିବା , 2.କǡ  କରିବା  (to abate 
stamp duty) , 3. ଉପଶମ  କରିବା  (The Act is 
now abated)  
abbreviate  (v) : ସଂେŁପ  କରିବା  
abbreviated  (a) : ସଂŁିƌ  
abbreviation  (n) : ସଂେŁପ , ଶƑ ସଂେŁପ  
abdicate  (v) : ପଦତȻାଗ  କରିବା  (to abdicate the 
post)  
abdication  (n) : ପଦତȻାଗ  
abduct  (v) : ଅପହରଣ  କରିବା  
abduction  (n) : ଅପହରଣ  
abductor  (n) : ଅପହରଣକାରୀ  
abet (v) : କୁȄେରାଚନା  େଦବା , ଖରାପ  କାମ କରିବା  ପାଇଁ 
Ȅବŧƽାଇବା  
abetment  (n) : କୁȄେରାଚନା , କୁକାଯƽȻ  ପାଇଁ େȄରଣା  
abettor  (n) : କୁȄେରାଚକ  """
    }
]