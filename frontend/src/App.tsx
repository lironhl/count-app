import { useEffect, useState } from 'react';
import { countApi } from './server';
import { Count } from './api';

function App() {
  const [counts, setCounts] = useState<Count[]>([])

  useEffect(() => {
    countApi
      .readCounts()
      .then(resp => {
        setCounts(resp.data)
      });
  }, [])

  const onCountClick = async () => {
    const resp = await countApi.createCount({ date: (new Date()).toJSON() });
    setCounts(counts => [...counts, resp.data])
  }

  return (
    <div className="App">
      <button onClick={onCountClick}>Count!</button>
      {counts.map(count => (
        <div key={count.id}>
          {count.date}
        </div>
      ))}
    </div>
  );
}

export default App;
