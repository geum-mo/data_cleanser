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
  - [x] Handle -s (dashes)
    - [x] Keep -s except being used as seperators
    - [x] Seperate rows based on -s
    - [x] Make sure remaining -s are not seperators
  - [ ] Hangle []s (square brackets)
    - [x] Remove whitespace in the start & end of the strings
    - [ ] Remove emtpy brackets []
    - [ ] 

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


