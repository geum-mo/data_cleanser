Cleansing raw data from NAVER V LIVE fansub platform to train a Google AutoML Translate's Korean > English translation engine.

Task flows:
- [x] Combine 2 csv files ("open" & "official") into one file ("combined")
- [x] Remove blank rows
  - [x] Delete rows containing NaN either in column 0 (Korean subs) or 1 (English subs)
- [x] Remove rows with inconsistent in using dashes and brackets
  - [x] Delete rows where each column has the unidentical number of -s (dashes)
  - [x] Delete rows where each column has the unidentical number of []s (square brackets with no string inside)
  - [x] Delete rows where each column has the unidentical number of [s (opening square bracket)
  - [x] Delete rows where each column has the unidentical number of ]s (closing square bracket)
- [ ] Seperate rows containing multiple sentences
  - [ ] Handle -s (dashes)
    - [ ] Check if any - (dash) without a single whitespace on the right and Print
    - [ ] Check if any - (dash) without a single whitespace on the left (if the dast is the first character of the value) and Print
    - [ ] Check if any - (dash) having no string next to its whitespace on the right and Print
    - [ ] 


  - [ ] Find rows containing - (dash) and Seperate into  
  - [ ] Find rows containing [] (empty square brackets) and Remove the brackets
  - [ ] Find rows containing [*]* (square brackets followed by string) and Seperate into 

- [ ] Handle special characters
  - [ ] ?
    - [ ] Only one ? should exist in a single row 
  - [ ] !
  - [ ] ~
  - [ ] . .. ... .... etc
  - [ ] , ,, ,,, ,,,, etc
  - [ ] []
  - [ ] {}
- [ ] Remove duplicated rows
- [ ] Create 3 tsv files for TRAIN, VALIDATION, and TEST purposes
  - [ ] For all purposes
    - [ ] Exclude  


