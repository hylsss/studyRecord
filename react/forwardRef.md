### forwardRef

forwardRef允许你的组件使用ref将一个DOM节点暴露给父组件。

```javascript
const SomeComponent = forwardRef(render)
```

定义ref组件：

`useImperativeHandle` 是 React 中的一个 hook，用于与父组件通信，向父组件暴露子组件的某些方法或属性。通常情况下，React 推荐使用 props 来进行组件之间的通信，但有时候需要在子组件中暴露一些方法给父组件调用，这时可以使用 `useImperativeHandle`。

```javascript
const ChildComponent = forwardRef((props, ref) => {
  const inputRef = useRef();

  // 将 inputRef 的方法暴露给父组件
  useImperativeHandle(ref, () => ({
    focusInput: () => {
      inputRef.current.focus();
    },
    // 可以暴露其他方法或属性...
  }));

  return <input ref={inputRef} />;
});
```

父组件里面调用:

```react
// 父组件
const ParentComponent = () => {
  const childRef = useRef();

  const handleFocusInput = () => {
    // 调用子组件暴露的 focusInput 方法
    childRef.current.focusInput();
  };

  return (
    <div>
      <ChildComponent ref={childRef} />
      <button onClick={handleFocusInput}>Focus Input</button>
    </div>
  );
};
```

