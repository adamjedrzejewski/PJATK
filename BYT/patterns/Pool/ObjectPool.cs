using System.Collections.Generic;

namespace Pool 
{
    public class ObjectPool
    {
        public int Size { get => _queue.Count; }     
        private Queue<Reusable> _queue = new Queue<Reusable>();
        private static ObjectPool _instance;

        private ObjectPool()
        {
            
        }

        public static ObjectPool GetInstance()
        {
            if (_instance == null)
            {
                _instance = new ObjectPool();
            }

            return _instance;
        }

        public Reusable GetReusable()
        {
            if (_queue.Count == 0)
            {
                return new Reusable();
            }
            else
            {
                var reusable = _queue.Dequeue();
                return reusable;
            }
        }

        public void PutReusable(Reusable reusable)
        {
            _queue.Enqueue(reusable);
        }
    }
}