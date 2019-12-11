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
- [x] Seperate rows containing multiple sentences
  - [x] Handle -s (dashes)
    - [x] Keep -s except being used as seperators
    - [x] Seperate rows based on -s
    - [x] Make sure remaining -s are not seperators
  - [x] Hangle []s (square brackets)
    - [x] Remove whitespace in the start & end of the strings
    - [x] Remove emtpy brackets, if any []
    - [ ] Handle scenarios
      - [ ] #1. [xx] --> keep as-is
      - [ ] #2. [xx]xx --> seperate rows
      - [ ] #3. xx[xx] --> seperate rows
      - [ ] #4. [xx][xx] --> seperate rows
      - [ ] #5. [xx[xx]] --> check and remove if trivial
      - [x] Just removed all rows with any [ in it

- [x] Handle duplicates
  - [x] Remove rows with NaNs
  - [x] Remove rows where string value of both columns are indentical
  - [x] Remove rows if string length is > 108 
  - [x] Remove duplicated based on source lang.
  
- [ ] Handle special characters
  - [ ] ?
    - [ ] Only one ? should exist in a single row 
  - [ ] !
  - [ ] ~
  - [ ] . .. ... .... etc
  - [ ] , ,, ,,, ,,,, etc
  - [ ] []
  - [ ] {}

- [ ] Detect any lang. other than Korean or English
- [ ] 


- [ ] Create 3 tsv files for TRAIN, VALIDATION, and TEST purposes
  - [ ] For all purposes
    - [ ] Exclude  


