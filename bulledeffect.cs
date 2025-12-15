using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
       Invoke("DestroyObject", 3f);

    }

    // Update is called once per frame
       void DestroyObject()
    {
        Destroy(gameObject);
    }
}
