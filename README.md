# Langtopia
Langtopia is the software that helps you to understand any language on your computer screen or audio sounds from your computer.

## Software Project Ⅱ AD Project
### 0. 시연 영상 및 자료
#### 0.1. 프로젝트 수행 보고서
* [요구사항명세서](./docs/SRS.md)
* [소프트웨어 구조 설계서](./docs/ADS.md)

#### 0.2. 발표 자료
* [소프트웨어 프로젝트2 AD Project 발표자료.pdf](./docs/소프트웨어%20프로젝트2%20AD%20Project%2004분반%203조.pdf)

#### 0.3. 시연 영상
[![YoutubeVid](http://img.youtube.com/vi/nfQMAQ8Ww1U/0.jpg)](http://www.youtube.com/watch?v=nfQMAQ8Ww1U)

### 1. Team Infos

* 팀명: 3조

* 팀 멤버:

| 이름   | 학번     |
|--------|----------|
| 윤상건 | 20191632 |
| 엄석현 | 20191623 |

### 2. About This Project

* 프로젝트 이름: Langtopia

* 프로젝트 목표: Langtopia를 사용하는 사용자가 컴퓨터 화면에 나타나는 영어로된 글씨나 영어로된 음성을 이해할 수 있도록 도와준다.

* 목표 달성을 위한 주요 기능: 
    * Screen Translator
        * 컴퓨터 화면에 출력되어 있는 문자를 인식 및 번역하여 사용자에게 번역 결과를 보기 좋게 보여주는 기능
    
    * Audio Subtitles
        * 자막 인식: 컴퓨터에서 출력되는 특정 길이의 소리 구간을 인식하여 해당 구간에 등록된 자막을 자동으로 출력하는 기능
        
        * 음성 인식: 컴퓨터에서 출력되는 음성을 인식하고 번역한 결과를 실시간으로 출력하는 기능
        
### 3. 실행 환경

* Audio Subtitles기능을 이용하기 위해서는, 윈도우 시스템 소리를 입력장치로 입력받기 위한 가상 오디오 케이블이 설치되어 있어야 한다.

    * 개발중에 사용한 가상 오디오 케이블은 [VoiceMeeter](https://www.vb-audio.com/Voicemeeter/) 프로그램을 이용했다. 해당 프로그램을 설치하여 기본 재생 장치를 `VoiceMeeter Input`으로 두고 기본 녹음 장치를 `VoiceMeeter Output`으로 두면 된다.