# Zustand
- 압도적 가벼움 (리코일의 1/20)
- 쉬운 사용법
- Flux 패턴의 상태관리 라이브러리

## Zustand 설치
- `npm i zustand`

## 스토어 생성
- src/store/store.ts
```js
import { create } from 'zustand'

// 타입스크립트에서는 써야하는 듯..?
interface userInfoType {
  bears: number
  increasePopulation: (by: number) => void
}

export const useStore = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 }),
}))

```

## 스토어 사용
- page.tsx에서 import 후 구조분해할당이나 한개씩 할당하여 활용

```js
import { userStore } from '폴더 경로/store.ts'


// 한번에 가져오기
const { bears, increasePopulation, removeAllBears } = useBearStore((state) => state)

// 하나씩 가져오기
const bears = useBearStore((state) => state.bears)
const increasePopulation = useBearStore((state) => state.increasePopulation)
const removeAllBears = useBearStore((state) => state.removeAllBears)

```
