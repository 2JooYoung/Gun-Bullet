# Gun & Bullet System (Maya Python Script)

## Overview
이 프로젝트는 Maya Python을 활용하여 **총(Gun)** 과 **총알(Bullet)** 을 생성하고,  
대상을 조준(`aim`)하고 발사(`shoot`)하여 **타겟 오브젝트를 제거**하는 기능을 구현한 것입니다.  


---

## Features

### 1. Gun 생성
Gun 클래스는 다음 요소로 구성됩니다:
- Barrel (총열)
- Handle (손잡이)
- Trigger Guard (방아쇠 덮개)
- Hidden Bullet (기본적으로 숨겨진 총알)

이 모든 구성 요소는 `polyCube`, `polyCylinder` 등을 사용해 생성되며,  
최종적으로 `polyUnite`를 통해 하나의 모델로 합쳐집니다.  


---

## Aim 기능
`gun.aim('target')` 을 실행하면 총이 지정된 타겟을 바라보도록 회전합니다.

- Maya의 `aimConstraint`를 활용해 방향을 맞춘 뒤  
- Constraint를 제거하여 회전만 남기도록 처리합니다.  


**결과:** 
총이 `pTorus1`을 바라보는 모습  

<img width="545" height="272" alt="image" src="https://github.com/user-attachments/assets/d949b5a9-dced-4ee5-8deb-f4142d4e684d" />

---

## Shoot 기능
`gun.shoot('target')` 실행 시 다음 순서로 진행됩니다:

1. 타겟의 월드 좌표를 가져옴  
2. 숨겨져 있던 Bullet을 해당 위치로 이동  
3. Bullet을 표시(show)  
4. 맞은 타겟 오브젝트 삭제  


**결과:**  
총알이 날아가 타겟 오브젝트가 사라짐  

<img width="564" height="281" alt="image" src="https://github.com/user-attachments/assets/41f8e756-b513-49c4-ab51-9ac91e789109" />


---

